import sys

from multiprocessing import freeze_support

from server.bert_serving.server.cli import main

try:
    # python 3.4+ should use builtin unittest.mock not mock package
    from unittest.mock import patch
except ImportError:
    from mock import patch

def test_parse_args():
    testargs = ["bert-serving-start", "-model_dir", "D:/data/bert/uncased_L-24_H-1024_A-16", 
                "-num_worker=1",
                "-tuned_model_dir", "D:/models/tmp/squad2_large/",
                "-ckpt_name", "model.ckpt-43439",
                "-pooling_layer", "-1", 
                "-pooling_strategy", "FIRST_TOKEN", # I believe SQuAD uses FIRST_TOKEN
                "-max_seq_len", "256", 
                "-max_batch_size", "16", 
                #"-show_tokens_to_client",
                "-squad" # my custom squad parameter
                ,"-http_port", "8125"
                ]
    with patch.object(sys, 'argv', testargs):
        main()

if __name__ == "__main__":
	freeze_support() # freeze support of multiprocessing - for debugging in visual studio, I think.
	test_parse_args()