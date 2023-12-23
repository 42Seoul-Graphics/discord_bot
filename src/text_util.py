import os
import json
import re
import subprocess
from datetime import datetime, timedelta

# 파일 메타데이터 및 태그 파싱 함수
def parse_file_metadata_and_tags(filepath, filename):
    folder = os.path.dirname(filepath)
    commit_counts_in_2weeks = int(os.popen("cd " + folder + " && git log --since=1.days --oneline " + filename + " | wc -l").read().strip())
    # 파일 내부에서 태그 파싱
    tags = set()
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            found_tags = re.findall(r'#\w+', line)
            tags.update(found_tags)

    return {
        'commit_counts_in_2weeks': commit_counts_in_2weeks,
        'tags': list(tags)
    }


def get_files_info():
  # 클론할 Git 리포지토리 URL
  repo_url = os.environ.get("REPO_URL")

  # 클론할 위치 및 디렉토리 이름
  clone_dir = os.environ.get("CLONE_DIR")
  res_data = []
  all_members = []

  # Git 클론 명령어 실행
  os.system("git clone " + repo_url + " " + clone_dir)
  # 각 마크다운 파일에 대해 메타데이터 및 태그 파싱
  for root, dirs, files in os.walk(clone_dir):
    writer = root.split('/')[-1]
    for filename in files:
      if filename.endswith(".md"):
        temp = {}
        filepath = os.path.join(root, filename)
        metadata = parse_file_metadata_and_tags(filepath, filename)
 
        temp['writer'] = writer
        temp['filename'] = filename
        temp['commit_counts_in_2weeks'] = metadata['commit_counts_in_2weeks']
        temp['tags'] = metadata['tags']
        res_data.append(temp)
  # 클론된 리포지토리 삭제
  # os.system("rm -rf " + clone_dir)
  return res_data

def get_uncompleted_member():
  uncompleted_members = []
  files = get_files_info()
  all_members = files[-1]['all_members']
  # for file in files:
    #  print(file)
  return uncompleted_members

def get_all_members():
  repo_url = os.environ.get("REPO_URL")
  clone_dir = os.environ.get("CLONE_DIR")
  all_members = []
  os.system("git clone " + repo_url + " " + clone_dir)
  for root, dirs, files in os.walk(clone_dir):
    if root == clone_dir:
      all_members = dirs
  all_members.remove('.git')
  return all_members





