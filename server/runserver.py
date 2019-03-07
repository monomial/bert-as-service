import sys

from multiprocessing import freeze_support

from server.bert_serving.server.cli import main

try:
    # python 3.4+ should use builtin unittest.mock not mock package
    from unittest.mock import patch
except ImportError:
    from mock import patch

def test_parse_args():
    testargs = ["bert-serving-start", "-model_dir", "C:\\Users\\michaels\\Projects\\bert\\models\\uncased_L-12_H-768_A-12", "-num_worker=1"]
    with patch.object(sys, 'argv', testargs):
        main()

if __name__ == "__main__":
	freeze_support() # freeze support of multiprocessing - for debugging in visual studio, I think.
	test_parse_args()