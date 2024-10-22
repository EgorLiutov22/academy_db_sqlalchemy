class Doctor:
    pass


class Patient:
    pass

def make_somebody(classname, **kwargs):
    classes = {'doctor': Doctor, 'patient': Patient}
    s = classes[classname]()
    return s

if __name__ == '__main__':
    m = make_somebody('doctor', name = 'John Doe')
    print(type(m))