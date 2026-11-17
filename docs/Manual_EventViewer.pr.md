



# Visualizador de Eventos do Windows
  
Módulo para ler e filtrar registros do Visualizador de Eventos do Windows.  

*Read this in other languages: [English](Manual_EventViewer.md), [Português](Manual_EventViewer.pr.md), [Español](Manual_EventViewer.es.md)*
  
![banner](imgs/BANNEREVENTVIEWER.jpg)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  



## Como usar este módulo
Este módulo permite ler e filtrar registros do Visualizador de Eventos do Windows.

1. **Registro:** Selecione o registro do Windows que você deseja consultar. Observe que o acesso ao registro de **Segurança** pode exigir permissões de administrador.

2. **Origem:** Permite filtrar os eventos de acordo com o nome de sua origem (por exemplo, `UserModePowerService`).

3. **ID do evento:** Permite filtrar os registros pelo identificador do evento.

4. **Tipo de evento:** Selecione o tipo de evento que você deseja incluir nos resultados.

5. **Desde:** Define a data e a hora iniciais para incluir os eventos gerados a partir desse momento.

6. **Até:** Define a data e a hora limite para incluir os eventos gerados até esse momento.

7. **Filtrado por mensagem:** O valor inserido deve corresponder exatamente ao nome da origem do evento (*Source*, por exemplo, `UserModePowerService`) ou a um código de erro específico incluído na descrição geral do evento. Este filtro
 não permite pesquisas por palavras-chave nem correspondências parciais de texto.

8. **Número máximo de registros a serem analisados:** Indica a quantidade máxima de registros que serão consultados, começando pelos mais recentes. Por padrão, são analisados 1.000 registros.

## Descrição do comando

### Obter eventos do Windows
  
Lê e filtra registros do Visualizador de Eventos do Windows.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Log|Selecione o log do Windows que deseja ler. Segurança pode exigir permissões de administrador.|Selecione o log|
|Origem contém|Filtra eventos cujo nome de origem contém este texto.|Opcional|
|ID do evento|Filtra por um ID de evento exato.|Opcional|
|Tipo de evento|Selecione o tipo de evento que deseja incluir nos resultados.|Selecione o tipo de evento|
|De (DD/MM/AAAA HHmmss)|Inclui eventos gerados a partir desta data e hora.|14/10/2026 10:57:15|
|Até (DD/MM/AAAA HHmmss)|Inclui eventos gerados até esta data e hora.|14/10/2026 10:57:15|
|Filtro de mensagem|Filtra eventos por origem ou código de erro específico.|Opcional|
|Máximo de registros a verificar|Número máximo de registros verificados, começando pelos mais recentes. Padrão 1000.|1000|
|Atribuir resultado à variável|Variável onde os resultados do log de eventos serão armazenados.|event_logs|
