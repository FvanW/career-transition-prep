import pytest
from unittest.mock import patch
import benchmark

@patch('timeit.timeit')
def test_benchmark_main(mock_timeit, capsys):
    # Mock timeit to return deterministic values
    # The first call is for baseline, the second for optimized
    mock_timeit.side_effect = [0.5, 0.25]

    benchmark.main()

    # Assert timeit was called correctly
    assert mock_timeit.call_count == 2
    mock_timeit.assert_any_call("test()", setup=benchmark.setup_baseline, number=100000)
    mock_timeit.assert_any_call("test()", setup=benchmark.setup_optimized, number=100000)

    # Assert correct output
    captured = capsys.readouterr()
    output = captured.out

    assert "Baseline:  0.5000s" in output
    assert "Optimized: 0.2500s" in output
    assert "Improvement: 50.00%" in output

@patch('timeit.timeit')
def test_benchmark_main_negative_improvement(mock_timeit, capsys):
    # Test when optimized is slower
    mock_timeit.side_effect = [0.25, 0.5]

    benchmark.main()

    captured = capsys.readouterr()
    output = captured.out

    assert "Baseline:  0.2500s" in output
    assert "Optimized: 0.5000s" in output
    assert "Improvement: -100.00%" in output
