import os, sys, zipfile, urllib
from copy import copy

class PluginManager(object):
    
    def __init__(self, folder):
        self.plugins_folder = folder
            
    def search_for_plugins(self):
        if not os.path.isdir(self.plugins_folder):
            os.makedirs(self.plugins_folder)
        self._plugins = {}
        
        plugs = os.listdir(self.plugins_folder)
        plugs = [p.replace('.py', '') for p in plugs if p.endswith('.py')]
        
        for plug in plugs:
            self._load_plugin(plug)

    def _load_plugin(self, plug):
        old_syspath = copy(sys.path)
        try:
            sys.path += [self.plugins_folder]
            module = __import__(plug, globals(), locals(), ['plugin'])
            instance = module.Plugin()
            self._plugins[instance._name] = instance
        except(ImportError, AttributeError), reason:
            print 'error loading "%s": %s' % (plug, reason)
        finally:
            sys.path = old_syspath
            
    def get_plugins(self):
        plugs = [self._plugins[name] for name in self._plugins.keys()]
        return plugs
        
    def get_active_show_plugins(self):
        plugs = []
        for name in self._plugins.keys():
            if self._plugins[name]._active and self._plugins[name]._toShow:
                plug = [self._plugins[name]._icon, name]
                plugs.append(plug)
        return plugs
