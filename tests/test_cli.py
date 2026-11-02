from textutils.cli import main


def test_cli_prints_all_results(capsys: object) -> None:
    exit_code = main(["Don't stop. Don't worry!"])

    captured = capsys.readouterr()  # type: ignore[attr-defined]

    assert exit_code == 0
    assert "Cleaned text" in captured.out
    assert "don't stop don't worry" in captured.out
    assert "Tokens" in captured.out
    assert "don't, stop, don't, worry" in captured.out
    assert "Word frequencies" in captured.out
    assert "don't: 2" in captured.out
    assert "stop: 1" in captured.out
    assert "worry: 1" in captured.out
