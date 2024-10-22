import inspect
import doctorandpatient

def make_somebody(classname, **kwargs):
    # classes = {'doctor': Doctor, 'patient': Patient}
    all_members = inspect.getmembers(doctorandpatient)
    classes = {str(m[0]).lower(): m[1] for m in all_members if inspect.isclass(m[1])}
    s = classes[classname]()
    return s

if __name__ == '__main__':
    m = make_somebody('doctor', name = 'John Doe')
    print(type(m))
