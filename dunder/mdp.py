class Container(object):

    def __contains__(self, item):
        if item:
            return True
        return False



c = Container()
print(1 in c)
print([] in c)