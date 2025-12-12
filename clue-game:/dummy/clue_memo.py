import tkinter as tk

# 1. 데이터 정의 (게임 항목)
suspects = ["Green", "Mustard", "Peacock", "Plum", "Scarlet", "White"]
weapons = ["Wrench", "Candlestick", "Dagger", "Revolver", "Lead Pipe", "Rope"]
rooms = ["Bathroom", "Library", "Billiard Room", "Garage", "Bedroom", "Lounge", "Kitchen", "Yard", "Dining Room"]

# 2. 메모 데이터를 저장할 dictionary
# 키: 항목 이름 (예: "Green", "Wrench"), 값: 메모 내용 (문자열)
memo_data = {}
for item in suspects + weapons + rooms:
    memo_data[item] = ""

# 3. 메모 창 관련 functions

def open_memo_window(item_name):
    """특정 항목에 대한 메모 입력 창 열기"""
    
    # 메모 창 생성
    memo_win = tk.Toplevel(root)
    memo_win.title(f"{item_name} Memo")
    
    # 닫기 버튼을 누르면 save_memo 함수 실행
    memo_win.protocol("WM_DELETE_WINDOW", lambda: save_memo(item_name, text_area, memo_win))

    tk.Label(memo_win, text=f"Enter the memo about '{item_name}':", padx=10, pady=5).pack()
    
    # 텍스트 입력 영역 (현재 저장된 메모를 표시)
    text_area = tk.Text(memo_win, width=40, height=10)
    text_area.insert(tk.END, memo_data[item_name])
    text_area.pack(padx=10, pady=5)
    
    # 저장
    save_btn = tk.Button(memo_win, text="Save & Quit", 
                         command=lambda: save_memo(item_name, text_area, memo_win))
    save_btn.pack(pady=5)

def save_memo(item_name, text_widget, window):
    """메모 내용 Save & Quit"""
    
    # 텍스트 위젯에서 내용 가져오기
    content = text_widget.get("1.0", tk.END).strip()
    
    # 전역 dict에 저장
    memo_data[item_name] = content
    
    window.destroy()

# 4. GUI 구성 함수

def create_item_list(parent_frame, title, item_list, start_row):
    """항목 리스트 (label, checkbox, memo button) 생성"""
    
    tk.Label(parent_frame, text=title, font=("Helvetica", 12, "bold"), 
             bg='gray', fg='white', width=30).grid(row=start_row, column=0, columnspan=3, pady=5)
    
    row_counter = start_row + 1
    for item in item_list:
        # 항목 이름 label
        tk.Label(parent_frame, text=item, width=10, anchor='w').grid(row=row_counter, column=0, padx=2)
        
        # 체크박스 (X/V 등 status 표시)
        # Tkinter Var (StringVar나 IntVar)를 사용하여 상태를 추적해야
        var = tk.StringVar(value='□')
        tk.Checkbutton(parent_frame, text="X", variable=var, onvalue="V", offvalue="X").grid(row=row_counter, column=1)
        
        # 메모
        tk.Button(parent_frame, text="Memo", 
                  command=lambda name=item: open_memo_window(name)).grid(row=row_counter, column=2, padx=2)
        
        row_counter += 1
    
    return row_counter # 다음 카테고리가 시작할 행 번호 반환

# 5. 메인 창 설정

root = tk.Tk()
root.title("Clue Mystery Memo")

main_frame = tk.Frame(root, padx=10, pady=10)
main_frame.pack()

# 용의자 목록 생성
next_row = create_item_list(main_frame, "Who?", suspects, 0)

# 무기 목록 생성
next_row = create_item_list(main_frame, "What?", weapons, next_row)

# 장소 목록 생성
create_item_list(main_frame, "Where?", rooms, next_row)

root.mainloop()
