import package.info as inf
import Lesson4.Human as h
import Lesson4.Student as s
print(inf.__name__)
print(dir(inf.Info))
info = inf.Info()
print(hasattr(info, "multiplier"))
print(hasattr(info, "multiplier1"))
print(hasattr(info, "showValue"))
print(hasattr(info, "__ge__"))
#print(getattr(info, "multiplier1",))#Throw exception
print(getattr(info, "multiplier", False))
print(callable(info.multiplier))
print(callable(info.showInfoList))
human = h.Human()
print(issubclass(inf.Info, h.Human))
print(issubclass(s.Student, h.Human))