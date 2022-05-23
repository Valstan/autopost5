from bin import RWFile



failik = RWFile(name='personal', patch='database')
failik.open()

failik.value.update({str('new_id'): 'final'})
failik.save()
