# 簡易消費紀錄統計系統
# 使用一個 list 管理所有消費紀錄，內含 dict (包含「項目」及「金額」)
records = []

while True:
    print("\n--- 消費紀錄統計系統 ---")
    print("1. 新增消費")
    print("2. 顯示消費明細")
    print("3. 顯示統計")
    print("4. 退出系統")
    print("-" * 24)

    choice = input("請選擇功能: ").strip()

    # 1. 新增消費
    if choice == "1":
        item = input("請輸入消費項目: ").strip()

        # 檢查金額格式與數值的迴圈
        while True:
            amount_str = input("請輸入金額: ").strip()

            # 檢查是否為空字串或包含非 ASCII 字元
            if not amount_str or not amount_str.isascii():
                print("請輸入大於 0 的數字，可包含小數點。")
                continue

            # 檢查小數點數量
            if amount_str.count(".") > 1:
                print("請輸入大於 0 的數字，可包含小數點。")
                continue

            # 移除第一個小數點，檢查其餘是否皆為數字
            check_str = amount_str.replace(".", "", 1)
            if not check_str.isdigit():
                print("請輸入大於 0 的數字，可包含小數點。")
                continue

            # 轉換為 float 進行數值檢查
            amount = float(amount_str)
            if amount <= 0:
                print("請輸入大於 0 的有效金額。")
                continue

            # 格式與數值皆正確，跳出金額輸入迴圈
            break

        # 將消費紀錄以 dict 形式加入 list 中
        record = {"項目": item, "金額": amount}
        records.append(record)
        print("新增成功。")

    # 2. 顯示消費明細
    elif choice == "2":
        if len(records) == 0:
            print("目前沒有消費紀錄。")
        else:
            print("\n--- 消費明細 ---")
            print(f"{'編號':<4}  {'項目':<10}  {'金額':>10}")
            print("-" * 28)

            # 使用者循序顯示
            for i in range(len(records)):
                no = i + 1
                item_name = records[i]["項目"]
                amount_val = records[i]["金額"]
                print(f"{no:>4}  {item_name:<10}  {amount_val:>10.2f}")

    # 3. 顯示統計
    elif choice == "3":
        if len(records) == 0:
            print("目前沒有消費紀錄。")
        else:
            count = len(records)
            total = 0.0

            for r in records:
                total += r["金額"]

            average = total / count

            print("\n--- 消費統計 ---")
            print(f"消費筆數: {count}")
            print(f"總金額: {total:.2f} 元")
            print(f"平均每筆金額: {average:.2f} 元")

            if total < 300:
                print("消費提醒: 消費不多")
            elif 300 <= total < 500:
                print("消費提醒: 注意控制消費")
            else:
                print("消費提醒: 已達提醒門檻")

    # 4. 退出系統
    elif choice == "4":
        print("系統已退出。")
        break
    # 其它錯誤選項
    else:
        print("選項錯誤，請重新選擇。")
