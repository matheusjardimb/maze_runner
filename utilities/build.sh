rm build/ -rf
rm dist/ -rf
rm maze_runner.egg-info
python setup.py sdist bdist_wheel
