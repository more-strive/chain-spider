### python3.8.9
### 1，安装虚拟环境  
  mkvirtualenv chain-spider -p python3.8
### 2，安装依赖  
  pip install -r requirement.txt
### 3，修改代理爬虫配置
  配置代理  ./proxy_pool/setting.py 修改DB_CONN
### 4，启动代理爬虫
  cd proxy_pool & sh start.sh
### 5，启动API接口服务
  sh start.sh