import json
from datetime import datetime


def _normalize_text(value):
    if value is None:
        return ""
    return str(value).strip()


def _parse_event_datetime(value, field_name):
    if not value:
        return None
    try:
        try:
            parsed = datetime.strptime(value, "%d/%m/%Y %H:%M:%S")
        except ValueError:
            parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        raise ValueError(
            "El campo {} debe tener formato DD/MM/AAAA HH:mm:ss, por ejemplo 14/10/2026 10:57:15".format(field_name)
        )
    if parsed.tzinfo is not None:
        parsed = parsed.astimezone().replace(tzinfo=None)
    return parsed


def _event_type_name(event_type):
    names = {
        1: "Error",
        2: "Warning",
        4: "Information",
        8: "Success Audit",
        16: "Failure Audit",
    }
    return names.get(event_type, str(event_type))


def get_event_logs(
    log_name=None,
    source_filter=None,
    event_id=None,
    event_type=None,
    message_filter=None,
    start_time=None,
    end_time=None,
    max_records=1000,
):
    import win32evtlog

    log_name = _normalize_text(log_name) or "Application"
    source_filter = _normalize_text(source_filter).casefold()
    event_id_filter = _normalize_text(event_id) or None
    event_type_filter = _normalize_text(event_type).casefold()
    message_filter = _normalize_text(message_filter).casefold()
    start_time = _parse_event_datetime(_normalize_text(start_time), "Desde")
    end_time = _parse_event_datetime(_normalize_text(end_time), "Hasta")

    try:
        max_records = int(_normalize_text(max_records) or "1000")
    except ValueError:
        raise ValueError("El máximo de registros debe ser un número entero")
    if max_records < 1:
        raise ValueError("El máximo de registros debe ser mayor que cero")

    if event_id_filter:
        try:
            event_id_filter = int(event_id_filter)
        except ValueError:
            raise ValueError("El ID del evento debe ser un número entero")

    accepted_types = {
        "error": 1,
        "warning": 2,
        "information": 4,
        "información": 4,
        "info": 4,
        "success audit": 8,
        "audit success": 8,
        "failure audit": 16,
        "audit failure": 16,
    }
    if event_type_filter:
        event_type_filter = accepted_types.get(event_type_filter, event_type_filter)
        try:
            event_type_filter = int(event_type_filter)
        except (TypeError, ValueError):
            raise ValueError("Tipo no válido: Error, Warning, Information, Success Audit o Failure Audit")

    handle = win32evtlog.OpenEventLog(None, log_name)
    events = []
    
    try:
        flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
        stop_reading = False

        while len(events) < max_records and not stop_reading:
            records = win32evtlog.ReadEventLog(handle, flags, 0)
            if not records:
                break

            for event in records:
                event_time = event.TimeGenerated

                
                if end_time and event_time > end_time:
                    continue

                
                if start_time and event_time < start_time:
                    stop_reading = True
                    break

                event_id_val = event.EventID & 0xFFFF
                if event_id_filter is not None and event_id_val != event_id_filter:
                    continue

                if event_type_filter and event.EventType != event_type_filter:
                    continue

                if source_filter and source_filter not in event.SourceName.casefold():
                    continue

                strings = [str(val) for val in (event.StringInserts or [])]
                message = " ".join(strings)
                if message_filter and message_filter not in message.casefold():
                    continue

                events.append({
                    "record_number": event.RecordNumber,
                    "time_generated": event_time.isoformat(),
                    "event_id": event_id_val,
                    "event_type": _event_type_name(event.EventType),
                    "source": event.SourceName,
                    "computer": event.ComputerName,
                    "category": event.EventCategory,
                    "user_sid": str(event.Sid) if event.Sid is not None else None,
                    "strings": strings,
                    "message": message,
                })

                if len(events) >= max_records:
                    break
    finally:
        win32evtlog.CloseEventLog(handle)

    return json.dumps(events, ensure_ascii=False)