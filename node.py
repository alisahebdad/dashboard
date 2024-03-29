from abc import ABC
import os
import logging
import json
import pprint

class node(ABC):
    def __init__(self,addr=None) -> None:
        super().__init__()
        self._addr = None
        self.img = None
        self.name = None
        self.crop = None
        self.text = None
        self.static_args = []
        self.pixel = None
        if addr is not  None:
            self.load(addr)
        
    def load(self,addr:str):
        self._addr = addr
        path = os.path.join(*self._addr)
        file = open(path)
        logging.info('load metafile from {}'.format(path))
        self._json = json.load(file)
        self.img = self._json['img']
        self.name = self._json['name']
        self.crop = self._json['crop']
        self.text = self._json['text']
        self.static_args = self._json['static_args']
        if 'pixel' in self._json:
            self.pixel = {
                'addr':self._json['pixel']['addr'],
                'color':self._json['pixel']['color']
            }
        else:
            self.pixel = None
        if 'imgProcessingMethod' in self._json:
            self.imgProcessingMethod = self._json['imgProcessingMethod']
        else:
            self.imgProcessingMethod = None

    def __repr__(self) -> str:
        payload = {
            'name':self.name,
            'img':self.img,
            'crop':self.crop,
            'text':self.text,
            'static_args':self.static_args
        }
        if self.pixel is not None:
            payload['pixel'] = self.pixel

        return pprint.pformat(payload,indent=4)


if __name__ == "__main__":

    n = node(['metadata','1.json'])    
    n2 = node()
    print (n2)
    logging.info('application run ...')
    print (n)