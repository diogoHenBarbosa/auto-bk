#!/usr/bin/env python3
import os
import shutil

ENV_HOME= os.getenv("HOME")
PATH_BACKUP= f"{ENV_HOME}/.backup"
PATH_PWD=os.getenv("PWD")

def no_backup_blacklist():
  file = open(f"{PATH_PWD}/no-backup.txt","r")
  rows = file.readlines()
  return rows

def blacklist():
  black_list_file = []
  for row in no_backup_blacklist():
    black_list_file.append(row.strip())
  return black_list_file

def folder_backup_exist():
  return os.path.exists(f"{ENV_HOME}/.backup")

def create_folder_backup():
  if folder_backup_exist():
    shutil.rmtree(PATH_BACKUP)
    os.mkdir(PATH_BACKUP)

def list_file_backup():
  file_list= []
  for file in os.listdir(ENV_HOME):
    if file in blacklist() or "." in file:
      continue
    file_list.append(file)
  return file_list

def copy_file():
  for file in list_file_backup():
    print(f"Copy file in {PATH_BACKUP}/{file}")
    shutil.copytree(ENV_HOME+"/"+file , PATH_BACKUP+"/"+file)

def compact_files():
  shutil.make_archive(f"{ENV_HOME}/.backup/backup", 'zip', PATH_BACKUP)
  
def main():
  create_folder_backup()
  copy_file()
  compact_files()
    
  
main()


