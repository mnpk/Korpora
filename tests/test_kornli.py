from Korpora import Korpora, KorNLIKorpus


def test_usage():
    kornli = Korpora.load('kornli')
    assert len(kornli.snli_train) == len(KorNLIKorpus().snli_train)
    kornli.snli_train[0]
    assert len(kornli.snli_train) == 550152
    assert len(kornli.xnli_dev) == 2490
    assert len(kornli.xnli_test) == 5010
    assert len(kornli.multinli_train) == 392702
    for example in kornli.snli_train:
        continue
