# 导入压缩所需要的包
import zipfile
# 导入 os 模块
import os
# 导入 os.path 模块
import os.path


# 1. 创建类
class ZFile(object):
    # 2. 初始化数据 filename-文件名；mode-方式；basedir-绝对路径
    def __init__(self, filename, mode="r", basedir=""):
        self.filename = filename
        self.mode = mode
        # 如果写入的方式为 w-写入，a-追加
        if self.mode in ("w", "a"):
            # 读取zip文件并设置
            self.zfile = zipfile.ZipFile(filename,
                                         self.mode,
                                         compression=zipfile.ZIP_DEFLATED)
        else:
            # 如果没有，默认
            self.zfile = zipfile.ZipFile(filename, self.mode)
        # 绝对路径
        self.basedir = basedir
        # 如果没写，则使用os.path.dirname自动补全
        if not self.basedir:
            self.basedir = os.path.dirname(filename)

    # 添加单个文件
    def addfile(self, path, arcname=None):
        # 路径移除 // , /
        path = path.replace("//", "/")
        #
        if not arcname:
            if path.startswith(self.basedir):
                arcname = path[len(self.basedir):]
            else:
                arcname = ''
        self.zfile.write(path, arcname)

    # 是否添加多个文件
    def addfiles(self, paths):
        for path in paths:
            if isinstance(path, tuple):
                self.addfile(*path)
            else:
                self.addfile(path)

    # 关闭
    def close(self):
        self.zfile.close()

    def extract_to(self, path):
        for p in self.zfile.namelist():
            self.extract(p, path)

    def extract(self, filename, path):
        if not filename.endswith("/"):
            f = os.path.join(path, filename)
            dir = os.path.dirname(f)
            if not os.path.exists(dir):
                os.makedirs(dir)
            self.zfile(f, "wb").write(self.zfile.read(filename))


def create(zfile, files):
    z = ZFile(zfile, 'w')
    z.addfiles(files)
    z.close()


def extract(zfile, path):
    z = ZFile(zfile)
    z.extract_to(path)
    z.close()
