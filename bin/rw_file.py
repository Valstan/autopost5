import json
import os


class RWFile:
    def __init__(self, patch, name, value=None):
        self.patch = patch
        self.name = name
        self.full_path = patch + '/' + name
        self.value = value
        self.examination_dir()
        self.examination_file()

    def open(self):
        with open(os.path.join(self.full_path + '.json'), 'r', encoding='utf-8') as f:
            self.value = json.load(f)
            return self.value

    def save(self):
        with open(os.path.join(self.full_path + '.json'), 'w', encoding='utf-8') as f:
            f.write(json.dumps(self.value, indent=2, ensure_ascii=False))

    def examination_file(self):
        if not os.path.exists(self.full_path + '.json'):
            with open(os.path.join(self.full_path + '.json'), 'w', encoding='utf-8') as f:
                f.write(json.dumps({}, indent=2, ensure_ascii=False))

    def examination_dir(self):
        if self.patch and not os.path.isdir(self.patch):
            os.makedirs(self.patch)

    # def rename(self):
    #    os.rename(self.name + '.json', 'old_' + self.name + '.json')
