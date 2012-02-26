import pickle

# Home grown - needs to know about model's innards

from ModelOo import Model, Thing

DEFAULT_FILENAME = "hexmodel_homegrown.txt"

class Persistence:
        
    def LoadAll(self, model, filename):
        if not filename:
            filename = DEFAULT_FILENAME
        output = open(filename, 'r')
        
        # Could also just create a new model e.g.
        #   model = Model()
        # since we return a model object
        # (whether its totally new or just the old existing one repopulated) 
        # and the layer above resets the app to use whatever we return here.
        model.Clear()
                                
        for line in output.readlines():
            model.AddThing(line.strip())
        output.close()
        
        return model

    def SaveAll(self, model, filename):
        if not filename:
            filename = DEFAULT_FILENAME
        output = open(filename, 'w')
        for thing in model.things:
            output.write(str(thing.info)+'\n')
        output.close()

        