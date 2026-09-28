from veritas.__main__ import main


def test_main_prints_message(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Start coding in Python today!"