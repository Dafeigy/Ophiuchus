import sys
from random import randint
from struct import pack
import time
from typing import Union

from io import BufferedReader

import sampler


class LTEncoder():
    def __init__(self, blocksize:int, file_name:str) -> None:
        self.blocksize = blocksize
        self.file_name = file_name
        pass

    def _split_file(self, source:Union[BufferedReader,str]):
        """
        Block file byte contents into blocksize chunks, padding last one if necessary
        """
        # TODO: Maybe f can be str or File Instance?
        if isinstance(source, BufferedReader):
            f_bytes = f.read()
        elif isinstance(source, str):
            f_bytes = str.encode(source)
        else:
            raise TypeError("Only BufferedReader or str supported.")
    
        # print(type(f_bytes),type(f))
        blocks = [int.from_bytes(f_bytes[i:i+self.blocksize].ljust(self.blocksize, b'0'), sys.byteorder) 
                for i in range(0, len(f_bytes), self.blocksize)]
        return len(f_bytes), blocks

    def _gen_blocks(self, source, seed=None, c=sampler.DEFAULT_C, delta=sampler.DEFAULT_DELTA):
        """Generates an infinite sequence of blocks to transmit
        to the receiver
        """

        # Generate seed if not provided
        if seed is None:
            seed = randint(0, 1 << 31 - 1)
        # get file blocks
        filesize, blocks = self._split_file(source)

        # init stream vars
        K = len(blocks)
        prng = sampler.PRNG(params=(K, delta, c))
        prng.set_seed(32)

        # block generation loop
        while True:
            blockseed, d, ix_samples = prng.get_src_blocks()
            block_data = 0
            for ix in ix_samples:
                block_data ^= blocks[ix]
            # print(f"d: {d}")
            # print(f"{ix_samples}")
            # Generate blocks of XORed data in network byte order
            block = (filesize, self.blocksize, blockseed, len(self.file_name.encode()), self.file_name.encode(), int.to_bytes(block_data, self.blocksize, sys.byteorder))
            # yield pack(f'!IIII{len(self.file_name.encode())}s{self.blocksize}s', *block)
            yield {
                'filesize':filesize,
                'self.blocksize': self.blocksize,
                'blockseed': blockseed,
                'data': int.to_bytes(block_data, self.blocksize, sys.byteorder)
            }

if __name__ == "__main__":
    lteconder = LTEncoder(32)
    test_str = "This is an implementation of a Luby Transform code in Python, consisting of two executables, one for each encoding and decoding files. These are thin wrappers around a core stream/file API."
    with open ("test.txt",'rb') as f:
        for block in lteconder._gen_blocks(f):
            pass
            # time.sleep(1)