from nicegui import ui

with ui.card().tight():
    ui.image('https://picsum.photos/id/684/640/360')

    with ui.card_section():
        ui.label('Lorem ipsum dolor sit amet, consectetur adipiscing elit, ...')

ui.run()