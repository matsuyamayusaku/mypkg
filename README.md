# mypkg
![test](https://github.com/matsuyamayusaku/mypkg/actions/workflows/test.yml/badge.svg)

ロボットシステム学の授業で作成したROS2のパッケージのリポジトリ

## 概要
### talker.py
* 数値をlistener.pyに送る
### listener.py
* talker.pyから送られた数値を出力
### talk_listen.launch.py
* talker.pyとlistener.pyのlaunchファイル

## リポジトリの使用方法
```
$ cd ~/ros2_ws/src/
$ git clone https://github.com/matsuyamayusaku/mypkg.git
$ cd ~/ros2_ws/
$ colcon build
```

## 実行方法
### talker listener
-実行
```
$ ros2 launch mypkg talk_listen.launch.py
```
-実行結果
```
[INFO] [launch]: All log files can be found below /home/yusaku/.ros/log/2023-01-21-18-42-09-398510-DESKTOP-LOBNNRA-611
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [612]
[INFO] [listener-2]: process started with pid [614]
[listener-2] [INFO] [1674294130.231837300] [listener]: Listen: 0
[listener-2] [INFO] [1674294130.712488100] [listener]: Listen: 1
[listener-2] [INFO] [1674294131.212759700] [listener]: Listen: 2
[listener-2] [INFO] [1674294131.712341600] [listener]: Listen: 3
[listener-2] [INFO] [1674294132.212573200] [listener]: Listen: 4
...
```

# テスト環境
* Ubuntu 20.04.5 LTS
* ROS2 noetic
* Python 3.7~3.10

## LICENSE
* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．


© 2022 Yusaku Matsuyama

