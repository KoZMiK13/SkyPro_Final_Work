results=./results
rep_history=./final-report/history
report=./final-report

rm -rf $results
python -m pytest --alluredir=$results
mv $rep_history $results
rm -rf $report
allure generate $results -o $report
allure open $report