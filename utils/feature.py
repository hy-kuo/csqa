"""
1. Feature.make(idx, tokens1, tokens2, tokensizer, max_seq_length)
2. Feature.make_single(idx, tokens1, tokenizer, max_seq_length)
"""


class Feature:
    def __init__(self, idx, input_ids, input_mask, segment_ids):
        self.idx = idx
        self.input_ids = input_ids
        self.input_mask = input_mask
        self.segment_ids = segment_ids

    @classmethod
    def make(cls, idx, tokens1, tokens2, tokenizer, max_seq_length):

        tokens = ['[CLS]'] + tokens1 + ['[SEP]'] + tokens2
        tokens = tokens[:max_seq_length-1]
        tokens = tokens + ['[SEP]']

        input_mask = [1] * len(tokens)
        segment_ids = [0] * (len(tokens1) + 2) + [1] * (len(tokens) - len(tokens1) - 2)

        input_ids = tokenizer.convert_tokens_to_ids(tokens)
        padding = [0] * (max_seq_length - len(input_ids))

        input_ids += padding
        input_mask += padding
        segment_ids += padding
        
        if len(segment_ids) > max_seq_length:
            segment_ids = segment_ids[:max_seq_length]
        
        # print("length of input_ids, input_mask, segment_ids,max_seq_length is {},{},{},{}".format(len(input_ids), len(input_mask), len(segment_ids), max_seq_length))
        assert len(input_ids) == len(input_mask) == len(segment_ids) == max_seq_length
        return cls(idx, input_ids, input_mask, segment_ids)

    @classmethod
    def make_single(cls, idx, tokens1, tokenizer, max_seq_length):
        # print(' '.join(tokens1))
        
        # token = ' '.join(tokens1).split('[SEP]')
        # question_length = 2 + len(token[0].split(' ')) + len(token[1].split(' '))

        tokens = ['[CLS]'] + tokens1
        tokens = tokens[:max_seq_length-1]
        tokens = tokens + ['[SEP]']

        input_mask = [1] * len(tokens)
        segment_ids = [1] * len(tokens)
        # segment_ids = [0] * question_length

        input_ids = tokenizer.convert_tokens_to_ids(tokens)
        padding = [0] * (max_seq_length - len(input_ids))
        # segment_padding = [1] * (max_seq_length - question_length)

        input_ids += padding
        input_mask += padding
        segment_ids += padding
        # segment_ids += segment_padding
        
        # print("max_seq_length is {}, segment_ids length is {}".format(max_seq_length, len(segment_ids)))

        return cls(idx, input_ids, input_mask, segment_ids)
        
    @classmethod
    def make_combined(cls, idx, tokens11, tokens12, tokens2, tokenizer, max_seq_length):

        tokens = ['[CLS]'] + tokens11 + ['[SEP]'] + tokens12
        sent_length = len(tokens)
        tokens = tokens + ['[SEP]'] + tokens2
        tokens = tokens[:max_seq_length-1]
        tokens = tokens + ['[SEP]']

        input_mask = [1] * len(tokens)
        segment_ids = [0] * sent_length

        input_ids = tokenizer.convert_tokens_to_ids(tokens)
        padding = [0] * (max_seq_length - len(input_ids))

        input_ids += padding
        input_mask += padding
        segment_ids += [1]  * (max_seq_length - sent_length)
        segment_ids = segment_ids[:max_seq_length]
        assert len(segment_ids) == max_seq_length
        # print("ids masks ids maxlength is {},{},{},{}".format(len(input_ids), len(input_mask), len(segment_ids), max_seq_length))

        return cls(idx, input_ids, input_mask, segment_ids)
        
class KBERTFeature:
    def __init__(self, idx, input_ids, input_mask, segment_ids):
        self.idx = idx
        self.input_ids = input_ids
        self.input_mask = input_mask
        self.segment_ids = segment_ids

    @classmethod
    def make(cls, idx, tokens1, tokens2, tokenizer, max_seq_length):

        tokens = ['[CLS]'] + tokens1 + ['[SEP]'] + tokens2
        tokens = tokens[:max_seq_length-1]
        tokens = tokens + ['[SEP]']

        input_mask = [1] * len(tokens)
        segment_ids = [0] * (len(tokens1) + 2) + [1] * (len(tokens) - len(tokens1) - 2)

        input_ids = tokenizer.convert_tokens_to_ids(tokens)
        padding = [0] * (max_seq_length - len(input_ids))

        input_ids += padding
        input_mask += padding
        segment_ids += padding
        
        if len(segment_ids) > max_seq_length:
            segment_ids = segment_ids[:max_seq_length]
        
        # print("length of input_ids, input_mask, segment_ids,max_seq_length is {},{},{},{}".format(len(input_ids), len(input_mask), len(segment_ids), max_seq_length))
        assert len(input_ids) == len(input_mask) == len(segment_ids) == max_seq_length
        return cls(idx, input_ids, input_mask, segment_ids)

    @classmethod
    def make_single(cls, idx, tokens1, tokenizer, max_seq_length):
        

        tokens = ['[CLS]'] + tokens1
        tokens = tokens[:max_seq_length-1]
        tokens = tokens + ['[SEP]']

        input_mask = [1] * len(tokens)
        segment_ids = [1] * len(tokens)

        input_ids = tokenizer.convert_tokens_to_ids(tokens)
        padding = [0] * (max_seq_length - len(input_ids))

        input_ids += padding
        input_mask += padding
        segment_ids += padding

        return cls(idx, input_ids, input_mask, segment_ids)
        
    @classmethod
    def make_combined(cls, idx, tokens11, tokens12, tokens2, tokenizer, max_seq_length):

        tokens = ['[CLS]'] + tokens11 + ['[SEP]'] + tokens12
        sent_length = len(tokens)
        tokens = tokens + ['[SEP]'] + tokens2
        tokens = tokens[:max_seq_length-1]
        tokens = tokens + ['[SEP]']

        input_mask = [1] * len(tokens)
        segment_ids = [0] * sent_length

        input_ids = tokenizer.convert_tokens_to_ids(tokens)
        padding = [0] * (max_seq_length - len(input_ids))

        input_ids += padding
        input_mask += padding
        segment_ids += [1]  * (max_seq_length - sent_length)
        segment_ids = segment_ids[:max_seq_length]
        assert len(segment_ids) == max_seq_length
        # print("ids masks ids maxlength is {},{},{},{}".format(len(input_ids), len(input_mask), len(segment_ids), max_seq_length))

        return cls(idx, input_ids, input_mask, segment_ids)

