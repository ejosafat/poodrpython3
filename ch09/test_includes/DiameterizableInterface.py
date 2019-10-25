from abc import ABC, abstractproperty


class DiameterizableInterfaceTest(ABC):
    @abstractproperty
    def object_tested(self):
        pass

    def test_implements_the_diameterizable_interface(self):
        self.assertTrue('diameter' in dir(self.object_tested))
