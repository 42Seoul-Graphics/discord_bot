import os
import json
import re
import subprocess
from datetime import datetime

# 파일 메타데이터 및 태그 파싱 함수
def parse_file_metadata_and_tags(filepath):
    ctime = os.path.getctime(filepath)  # 생성 시간
    mtime = os.path.getmtime(filepath)  # 수정 시간

    # 파일 내부에서 태그 파싱
    tags = set()
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            found_tags = re.findall(r'#\w+', line)
            tags.update(found_tags)

    return {
        'ctime': datetime.fromtimestamp(ctime).strftime('%Y-%m-%d %H:%M:%S'),
        'mtime': datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M:%S'),
        'tags': list(tags)
    }


def get_files_info():
	# 클론할 Git 리포지토리 URL
	repo_url = os.environ.get("REPO_URL")

	# 클론할 위치 및 디렉토리 이름
	clone_dir = os.environ.get("CLONE_DIR")
	text = ""

	# Git 클론 명령어 실행
	subprocess.run(["git", "clone", repo_url, clone_dir])
	# 각 마크다운 파일에 대해 메타데이터 및 태그 파싱
	for root, dirs, files in os.walk(clone_dir):
		writer = root.split('/')[-1]
		print("\n\nroot: ",root)
		print("\ndirs: ", dirs)
		print("\nfiles: ", files,"\n\n")

		for filename in files:
			if filename.endswith(".md"):
				filepath = os.path.join(root, filename)
				metadata = parse_file_metadata_and_tags(filepath)
				text += "SOMTHING"
				# 파일이 이전 격주 화요일 이후에 생성되었는지 확인


				print(f"Writer: {writer}")
				print(f"File: {filename}")
				print(f"Creation Time: {metadata['ctime']}")
				print(f"Modification Time: {metadata['mtime']}")
				print(f"Tags: {metadata['tags']}\n")

	# 클론된 리포지토리 삭제
	subprocess.run(["rm", "-rf", clone_dir])
	return text

def get_uncompleted_member():
	uncompleted_members = []
	files = get_files_info()
	#  TODO: file info 를 통해 안 한사람들 명단 반환

	uncompleted_members.append('test: ')
	uncompleted_members.append('seongyle')
	return uncompleted_members






