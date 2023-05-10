# coverage
```
% coverage run -m pytest
========================================================================= test session starts ==========================================================================
platform darwin -- Python 3.9.16, pytest-7.2.2, pluggy-1.0.0
rootdir: /Users/nlou/workspace/coverage
plugins: asyncio-0.21.0, requests-mock-1.10.0, xdist-3.2.1, common-tools-1.2.1755, cov-4.0.0, aiohttp-1.0.4
asyncio: mode=strict
collected 1 item                                                                                                                                                       

test_config.py .                                                                                                                                                 [100%]

========================================================================== 1 passed in 0.03s ===========================================================================
nlou@C02GN17Q1PG2 /Users/nlou/workspace/coverage [master]
% coverage lcov         
Traceback (most recent call last):
  File "/Users/nlou/.pyenv/versions/3.9.16/bin/coverage", line 8, in <module>
    sys.exit(main())
  File "/Users/nlou/.pyenv/versions/3.9.16/lib/python3.9/site-packages/coverage/cmdline.py", line 974, in main
    status = CoverageScript().command_line(argv)
  File "/Users/nlou/.pyenv/versions/3.9.16/lib/python3.9/site-packages/coverage/cmdline.py", line 746, in command_line
    total = self.coverage.lcov_report(
  File "/Users/nlou/.pyenv/versions/3.9.16/lib/python3.9/site-packages/coverage/control.py", line 1257, in lcov_report
    return render_report(self.config.lcov_output, LcovReporter(self), morfs, self._message)
  File "/Users/nlou/.pyenv/versions/3.9.16/lib/python3.9/site-packages/coverage/report.py", line 59, in render_report
    ret = reporter.report(morfs, outfile=outfile)
  File "/Users/nlou/.pyenv/versions/3.9.16/lib/python3.9/site-packages/coverage/lcovreport.py", line 45, in report
    self.get_lcov(fr, analysis, outfile)
  File "/Users/nlou/.pyenv/versions/3.9.16/lib/python3.9/site-packages/coverage/lcovreport.py", line 72, in get_lcov
    line = source_lines[covered-1].encode("utf-8")
IndexError: list index out of range

% coverage xml                       
Wrote XML report to coverage.xml
```

