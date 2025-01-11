import pandas as pd
import os

def get_file_paths(directorys):
    file_paths = []
    for directory in directorys:
        for dirpath, _, filenames in os.walk(directory):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                file_paths.append(file_path)
    return file_paths

directory_lihu = ['Train\\Lihu\\train', 'Train\\Lihu\\val', 'Test\\Lihu-test']
directory_longhua = ['Train\\Longhua\\train', 'Train\\Longhua\\val', 'Test\\Longhua-test']
directory_qingdao = ['Train\\Qingdao\\train', 'Train\\Qingdao\\val', 'Test\\Qingdao-test']
directory_wuhu = ['Train\\Wuhu\\train', 'Train\\Wuhu\\val', 'Test\\Wuhu-test']
directory_yuehai = ['Train\\Yuehai\\train', 'Train\\Yuehai\\val', 'Test\\Yuehai-test']
file_paths_lihu = get_file_paths(directory_lihu)
file_paths_longhua = get_file_paths(directory_longhua)
file_paths_qingdao = get_file_paths(directory_qingdao)
file_paths_wuhu = get_file_paths(directory_wuhu)
file_paths_yuehai = get_file_paths(directory_yuehai)

index = 0
tot = str(len(file_paths_lihu))
print("Handling Lihu ..." + tot + " areas to do.")

for file_path in file_paths_lihu:
    index += 1
    df = pd.read_csv(file_path, sep=' ', header=None)
    file_name, extension = os.path.splitext(os.path.basename(file_path))
    print("Handling " + file_name + "...[" + str(index) + "/" + tot + "]")
    df = df.drop([8], axis=1)

    create_path = f"UrbanBIS_to_S3DIS\\Area_1\\{file_name}\\Annotations\\"
    if not os.path.exists(os.path.dirname(create_path)):
        os.makedirs(os.path.dirname(create_path))

    df_entire_area = df.drop([6, 7], axis=1)
    df_entire_area.to_csv(f"UrbanBIS_to_S3DIS\\Area_1\\{file_name}\\{file_name}{extension}", sep=' ', index=False,
                          header=False)

    lable_name = ""
    lable_index = df[6].value_counts()
    for lable in lable_index.index:
        if lable == 0:
            lable_name = "terrain"
        elif lable == 1:
            lable_name = "vegetation"
        elif lable == 2:
            lable_name = "water"
        elif lable == 3:
            lable_name = "bridge"
        elif lable == 4:
            lable_name = "vehicle"
        elif lable == 5:
            lable_name = "boat"
        elif lable == 6:
            continue
        lable_name = lable_name + "_1"
        instance_df = df[df[6] == lable]
        instance_df = instance_df.drop([6, 7], axis=1)
        export_path = create_path + f"{lable_name}.txt"
        instance_df.to_csv(export_path, sep=' ', index=False, header=False)

    lable_index = df[7].value_counts()
    for lable in lable_index.index:
        if lable == -100:
            continue
        instance_df = df[df[7] == lable]
        instance_df = instance_df.drop([6, 7], axis=1)
        instance_lable_name = "building_" + str(lable)
        export_path = create_path + f"{instance_lable_name}.txt"
        instance_df.to_csv(export_path, sep=' ', index=False, header=False)

index = 0
tot = str(len(file_paths_longhua))
print("Handling Longhua ..." + tot + " areas to do.")

for file_path in file_paths_longhua:
    index += 1
    df = pd.read_csv(file_path, sep=' ', header=None)
    file_name, extension = os.path.splitext(os.path.basename(file_path))
    print("Handling " + file_name + "...[" + str(index) + "/" + tot + "]")
    df = df.drop([8], axis=1)

    create_path = f"UrbanBIS_to_S3DIS\\Area_2\\{file_name}\\Annotations\\"
    if not os.path.exists(os.path.dirname(create_path)):
        os.makedirs(os.path.dirname(create_path))

    df_entire_area = df.drop([6, 7], axis=1)
    df_entire_area.to_csv(f"UrbanBIS_to_S3DIS\\Area_2\\{file_name}\\{file_name}{extension}", sep=' ', index=False,
                          header=False)

    lable_name = ""
    lable_index = df[6].value_counts()
    for lable in lable_index.index:
        if lable == 0:
            lable_name = "terrain"
        elif lable == 1:
            lable_name = "vegetation"
        elif lable == 2:
            lable_name = "water"
        elif lable == 3:
            lable_name = "bridge"
        elif lable == 4:
            lable_name = "vehicle"
        elif lable == 5:
            lable_name = "boat"
        elif lable == 6:
            continue
        lable_name = lable_name + "_1"
        instance_df = df[df[6] == lable]
        instance_df = instance_df.drop([6, 7], axis=1)
        export_path = create_path + f"{lable_name}.txt"
        instance_df.to_csv(export_path, sep=' ', index=False, header=False)

    lable_index = df[7].value_counts()
    for lable in lable_index.index:
        if lable == -100:
            continue
        instance_df = df[df[7] == lable]
        instance_df = instance_df.drop([6, 7], axis=1)
        instance_lable_name = "building_" + str(lable)
        export_path = create_path + f"{instance_lable_name}.txt"
        instance_df.to_csv(export_path, sep=' ', index=False, header=False)

index = 0
tot = str(len(file_paths_qingdao))
print("Handling Qingdao ..." + tot + " areas to do.")

for file_path in file_paths_qingdao:
    index += 1
    df = pd.read_csv(file_path, sep=' ', header=None)
    file_name, extension = os.path.splitext(os.path.basename(file_path))
    print("Handling " + file_name + "...[" + str(index) + "/" + tot + "]")
    df = df.drop([8], axis=1)

    create_path = f"UrbanBIS_to_S3DIS\\Area_3\\{file_name}\\Annotations\\"
    if not os.path.exists(os.path.dirname(create_path)):
        os.makedirs(os.path.dirname(create_path))

    df_entire_area = df.drop([6, 7], axis=1)
    df_entire_area.to_csv(f"UrbanBIS_to_S3DIS\\Area_3\\{file_name}\\{file_name}{extension}", sep=' ', index=False,
                          header=False)

    lable_name = ""
    lable_index = df[6].value_counts()
    for lable in lable_index.index:
        if lable == 0:
            lable_name = "terrain"
        elif lable == 1:
            lable_name = "vegetation"
        elif lable == 2:
            lable_name = "water"
        elif lable == 3:
            lable_name = "bridge"
        elif lable == 4:
            lable_name = "vehicle"
        elif lable == 5:
            lable_name = "boat"
        elif lable == 6:
            continue
        lable_name = lable_name + "_1"
        instance_df = df[df[6] == lable]
        instance_df = instance_df.drop([6, 7], axis=1)
        export_path = create_path + f"{lable_name}.txt"
        instance_df.to_csv(export_path, sep=' ', index=False, header=False)

    lable_index = df[7].value_counts()
    for lable in lable_index.index:
        if lable == -100:
            continue
        instance_df = df[df[7] == lable]
        instance_df = instance_df.drop([6, 7], axis=1)
        instance_lable_name = "building_" + str(lable)
        export_path = create_path + f"{instance_lable_name}.txt"
        instance_df.to_csv(export_path, sep=' ', index=False, header=False)

index = 0
tot = str(len(file_paths_wuhu))
print("Handling Wuhu ..." + tot + " areas to do.")

for file_path in file_paths_wuhu:
    index += 1
    df = pd.read_csv(file_path, sep=' ', header=None)
    file_name, extension = os.path.splitext(os.path.basename(file_path))
    print("Handling " + file_name + "...[" + str(index) + "/" + tot + "]")
    df = df.drop([8], axis=1)

    create_path = f"UrbanBIS_to_S3DIS\\Area_4\\{file_name}\\Annotations\\"
    if not os.path.exists(os.path.dirname(create_path)):
        os.makedirs(os.path.dirname(create_path))

    df_entire_area = df.drop([6, 7], axis=1)
    df_entire_area.to_csv(f"UrbanBIS_to_S3DIS\\Area_4\\{file_name}\\{file_name}{extension}", sep=' ', index=False,
                          header=False)

    lable_name = ""
    lable_index = df[6].value_counts()
    for lable in lable_index.index:
        if lable == 0:
            lable_name = "terrain"
        elif lable == 1:
            lable_name = "vegetation"
        elif lable == 2:
            lable_name = "water"
        elif lable == 3:
            lable_name = "bridge"
        elif lable == 4:
            lable_name = "vehicle"
        elif lable == 5:
            lable_name = "boat"
        elif lable == 6:
            continue
        lable_name = lable_name + "_1"
        instance_df = df[df[6] == lable]
        instance_df = instance_df.drop([6, 7], axis=1)
        export_path = create_path + f"{lable_name}.txt"
        instance_df.to_csv(export_path, sep=' ', index=False, header=False)

    lable_index = df[7].value_counts()
    for lable in lable_index.index:
        if lable == -100:
            continue
        instance_df = df[df[7] == lable]
        instance_df = instance_df.drop([6, 7], axis=1)
        instance_lable_name = "building_" + str(lable)
        export_path = create_path + f"{instance_lable_name}.txt"
        instance_df.to_csv(export_path, sep=' ', index=False, header=False)

index = 0
tot = str(len(file_paths_yuehai))
print("Handling Yuehai ..." + tot + " areas to do.")

for file_path in file_paths_yuehai:
    index += 1
    df = pd.read_csv(file_path, sep=' ', header=None)
    file_name, extension = os.path.splitext(os.path.basename(file_path))
    print("Handling " + file_name + "...[" + str(index) + "/" + tot + "]")
    df = df.drop([8], axis=1)

    create_path = f"UrbanBIS_to_S3DIS\\Area_5\\{file_name}\\Annotations\\"
    if not os.path.exists(os.path.dirname(create_path)):
        os.makedirs(os.path.dirname(create_path))

    df_entire_area = df.drop([6, 7], axis=1)
    df_entire_area.to_csv(f"UrbanBIS_to_S3DIS\\Area_5\\{file_name}\\{file_name}{extension}", sep=' ', index=False,
                          header=False)

    lable_name = ""
    lable_index = df[6].value_counts()
    for lable in lable_index.index:
        if lable == 0:
            lable_name = "terrain"
        elif lable == 1:
            lable_name = "vegetation"
        elif lable == 2:
            lable_name = "water"
        elif lable == 3:
            lable_name = "bridge"
        elif lable == 4:
            lable_name = "vehicle"
        elif lable == 5:
            lable_name = "boat"
        elif lable == 6:
            continue
        lable_name = lable_name + "_1"
        instance_df = df[df[6] == lable]
        instance_df = instance_df.drop([6, 7], axis=1)
        export_path = create_path + f"{lable_name}.txt"
        instance_df.to_csv(export_path, sep=' ', index=False, header=False)

    lable_index = df[7].value_counts()
    for lable in lable_index.index:
        if lable == -100:
            continue
        instance_df = df[df[7] == lable]
        instance_df = instance_df.drop([6, 7], axis=1)
        instance_lable_name = "building_" + str(lable)
        export_path = create_path + f"{instance_lable_name}.txt"
        instance_df.to_csv(export_path, sep=' ', index=False, header=False)