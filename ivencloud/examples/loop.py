import ivencloud

print 'started'
acr = ivencloud.activate_device("9a03deafb9e47da404522e03f1145edb7d9c3b97", "cc3200")
print acr.__dict__

data = {
    'key1': 123,
    'key2': 'string'
}

i = 0


def my_callback(val):
    """
    Send data 3 times then stop loop

    :param val:
    :return:
    """

    global i
    print val.__dict__
    i += 1

    if i == 3:
        ivencloud.break_sendloop()


ivencloud.send_data_wloop(data, 3, my_callback)

print 'exit'
