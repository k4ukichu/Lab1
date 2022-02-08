From flask_table import Table,Col

class Data(Table):
    isbn =Col('ISBN')
    title =Col('Title')
    author =Col('Author')
    Published =Col('Date Published')

    Class comment(TAble):
    id =Col('comment Number')
    name =Col('Author')
    body =Col('Text')
    timestamp =Col('Time Posted') 