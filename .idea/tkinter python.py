'''
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw

# Helper function to create circular image
def create_circle_image(image_path, size):
    try:
        img = Image.open(image_path).resize((size, size), Image.Resampling.LANCZOS)
        circle = Image.new("L", (size, size), 0)
        draw = ImageDraw.Draw(circle)
        draw.ellipse((0, 0, size, size), fill=255)
        alpha = Image.new("L", img.size, 255)
        img.putalpha(circle)
        return ImageTk.PhotoImage(img)
    except:
        placeholder = Image.new("RGB", (size, size), color="gray")
        return ImageTk.PhotoImage(placeholder)
# 알림 데이터
notifications = [
    {"club": "그림 동아리", "message": "그림 과제 제출 완료", "image": "art club.jpg"},
    {"club": "영화 동아리", "message": "이번주 7/23일 모임 공지 ...", "image": "movie club.jpg"},
    {"club": "코딩 동아리", "message": "새 자료가 등록되었습니다\ncode.py", "image": "coding club.jpg"},
    {"club": "영어 회화 동아리", "message": "모임 장소 변경 안내 ...", "image": "english club.jpg"},
    {"club": "발표 동아리", "message": "코멘트가 등록되었습니다\n한글 파일 첨부 hwp", "image": "presentation club.jpg"},
    {"club": "베이킹 동아리", "message": "활동 사진이 등록되었습니다", "image": "baking club1.jpg"},
    {"club": "발표 동아리", "message": "이번주 7/25일 모임 공지\n발표 준비 해오세요", "image": "presentation club.jpg"},
]


# 초기 데이터
community_data = [
    {"type": "사진", "title": "2024-07-01 활동 사진"},
    {"type": "동영상", "title": "토론발표 영상", "description": "업로드 | 3일 전"},
    {"type": "파일", "title": "2기 코딩 동아리 지원 양식.pdf"},
    {"type": "코드 소스", "title": "code.py"}
]

mypage_data = [
    {"club": "코딩 동아리", "members": 50, "duration": "1학기, 2024년 6월 ~ 현재"},
    {"club": "영어 회화 동아리", "members": 30, "duration": "1학기, 2024년 7월 ~ 현재"},
    {"club": "탁구 동아리", "members": 70, "duration": "1년, 2024년 1월 ~ 현재"},
    {"club": "그림 동아리", "members": 20, "duration": "1년, 2024년 3월 ~ 현재"}
]

clubs = {
    "지원한 동아리": [{"name": "그림 동아리", "image": "art club.jpg"}, {"name": "영화 동아리", "image": "movie club.jpg"}],
    "현재 활동 중인 동아리": [{"name": "코딩 동아리", "image": "coding club.jpg"}, {"name": "영어 회화 동아리", "image": "english club.jpg"}],
    "찜한 동아리": [{"name": "발표 동아리", "image": "presentation club.jpg"}, {"name": "베이킹 동아리", "image": "baking club1.jpg"}]
}

# 마이페이지 화면
def show_my_page():
    for widget in main_frame.winfo_children():
        widget.destroy()

    tk.Label(main_frame, text="마이페이지", font=("Arial", 16, "bold")).pack(pady=10)

    canvas = tk.Canvas(main_frame)
    scrollable_frame = ttk.Frame(canvas)
    scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    for section, club_list in clubs.items():
        section_label = tk.Label(scrollable_frame, text=section, font=("Arial", 16, "bold"), anchor="w")
        section_label.pack(fill="x", padx=10, pady=5)

        for club in club_list:
            club_frame = ttk.Frame(scrollable_frame)
            club_frame.pack(fill="x", padx=10, pady=5)

            # Add circular image
            image = create_circle_image(club["image"], 50)
            img_label = tk.Label(club_frame, image=image)
            img_label.image = image
            img_label.pack(side="left", padx=5)

            # Add club name
            name_label = tk.Label(club_frame, text=club["name"], font=("Arial", 14))
            name_label.pack(side="left", padx=10)

# 자료실 화면
def show_community():
    for widget in main_frame.winfo_children():
        widget.destroy()

    tk.Label(main_frame, text="동아리 커뮤니티 자료실", font=("Arial", 16, "bold")).pack(pady=10)

    canvas = tk.Canvas(main_frame)
    scrollable_frame = ttk.Frame(canvas)
    scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    # 기존 자료 표시
    for resource in community_data:
        res_frame = ttk.Frame(scrollable_frame)
        res_frame.pack(fill="x", padx=10, pady=5)

        # Add resource type and title
        type_label = tk.Label(res_frame, text=resource["type"], font=("Arial", 12, "bold"), width=10, anchor="w")
        type_label.pack(side="left", padx=5)

        title_label = tk.Label(res_frame, text=resource["title"], font=("Arial", 12), anchor="w")
        title_label.pack(side="left", padx=10)

    # Add upload section
    upload_frame = ttk.Frame(scrollable_frame)
    upload_frame.pack(fill="x", pady=20)

    # Title entry
    title_label = tk.Label(upload_frame, text="자료 제목", font=("Arial", 12))
    title_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    title_entry = ttk.Entry(upload_frame, width=40)
    title_entry.grid(row=0, column=1, padx=10, pady=5)

    # Content entry (Text Widget)
    content_label = tk.Label(upload_frame, text="자료 내용", font=("Arial", 12))
    content_label.grid(row=1, column=0, padx=10, pady=5, sticky="nw")
    content_entry = tk.Text(upload_frame, width=40, height=10, wrap="word", font=("Arial", 10))
    content_entry.grid(row=1, column=1, padx=10, pady=5)

    # Upload button
    def upload_resource():
        title = title_entry.get()
        content = content_entry.get("1.0", "end").strip()  # Fetch content from Text widget
        if title and content:
            messagebox.showinfo("등록 완료", f"자료 '{title}'가 등록되었습니다!")
            title_entry.delete(0, "end")
            content_entry.delete("1.0", "end")
        else:
            messagebox.showwarning("경고", "자료 제목과 내용을 모두 입력하세요.")

    upload_button = ttk.Button(upload_frame, text="등록하기", command=upload_resource)
    upload_button.grid(row=2, column=1, pady=10, sticky="e")

    def add_data():
        new_data = {"type": "새 자료", "title": title_entry.get(), "description": content_entry.get()}
        community_data.append(new_data)
        show_community()




# 알림 공지 화면
def show_notifications():
    for widget in main_frame.winfo_children():
        widget.destroy()

    tk.Label(main_frame, text="동아리 알림 공지", font=("Arial", 16, "bold")).pack(pady=10)

    canvas = tk.Canvas(main_frame)
    scrollable_frame = ttk.Frame(canvas)
    scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    for notification in notifications:
        noti_frame = ttk.Frame(scrollable_frame)
        noti_frame.pack(fill="x", padx=10, pady=5)

        # Add circular image
        image = create_circle_image(notification["image"], 50)
        img_label = tk.Label(noti_frame, image=image)
        img_label.image = image
        img_label.pack(side="left", padx=5)

        # Add notification text
        text_label = tk.Label(noti_frame, text=f"{notification['club']}\n{notification['message']}",
                              font=("Arial", 12))
        text_label.pack(side="left", padx=10)


# Main App
root = tk.Tk()
root.title("동아리 앱")
root.geometry("300x500")

# Sidebar
sidebar = tk.Frame(root, width=200, bg="grey")
sidebar.pack(side="left", fill="y")

main_frame = tk.Frame(root)
main_frame.pack(side="right", fill="both", expand=True)

tk.Button(sidebar, text="동아리 알림 공지", command=show_notifications, width=15).pack(pady=10)
tk.Button(sidebar, text="자료실, 커뮤니티", command=show_community, width=15).pack(pady=10)
tk.Button(sidebar, text="마이페이지", command=show_my_page, width=15).pack(pady=10)


# Start with My Page
show_my_page()

root.mainloop()
'''



'''
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw


# Helper function to create circular image
def create_circle_image(image_path, size):
    try:
        img = Image.open(image_path).resize((size, size), Image.Resampling.LANCZOS)
        circle = Image.new("L", (size, size), 0)
        draw = ImageDraw.Draw(circle)
        draw.ellipse((0, 0, size, size), fill=255)
        alpha = Image.new("L", img.size, 255)
        img.putalpha(circle)
        return ImageTk.PhotoImage(img)
    except:
        placeholder = Image.new("RGB", (size, size), color="gray")
        return ImageTk.PhotoImage(placeholder)


# Sample data
notifications = [
    {"club": "그림 동아리", "text": "그림 과제 제출 완료", "image": "art club.jpg"},
    {"club": "영화 동아리", "text": "이번주 7/23일 모임 공지 ...", "image": "movie club.jpg"},
    {"club": "코딩 동아리", "text": "새 자료가 등록되었습니다", "image": "coding club.jpg"},
]

resources = [
    {"type": "사진", "title": "2024-07-01 활동 사진"},
    {"type": "동영상", "title": "토론발표 영상\n업로드 | 3일 전"},
    {"type": "파일", "title": "2기 코딩 동아리 지원 양식.pdf"},
]

clubs = {
    "지원한 동아리": [{"name": "그림 동아리", "image": "art club.jpg"}],
    "현재 활동 중인 동아리": [{"name": "코딩 동아리", "image": "coding club.jpg"}],
}


# Main application
class ClubApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("동아리 앱")
        self.geometry("300x500")

        # Tabs
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)

        # Create Frames
        self.create_notification_tab()
        self.create_resource_tab()
        self.create_mypage_tab()

    def create_scrollable_canvas(self, parent):
        canvas = tk.Canvas(parent, width=280, height=500)
        scrollbar = ttk.Scrollbar(parent, orient="vertical", command=canvas.yview)

        scrollable_frame = ttk.Frame(canvas)

        # Scroll configuration
        scrollable_frame.bind(
            "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        return scrollable_frame

    def open_detail_window(self, title, content):
        detail_window = tk.Toplevel(self)
        detail_window.title(title)
        detail_window.geometry("300x300")

        label = tk.Label(detail_window, text=content, wraplength=280, justify="left")
        label.pack(pady=10)

        close_button = ttk.Button(
            detail_window, text="닫기", command=detail_window.destroy
        )
        close_button.pack(pady=10)

    def create_notification_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="동아리 알림")

        scrollable_frame = self.create_scrollable_canvas(frame)

        for notification in notifications:
            noti_frame = ttk.Frame(scrollable_frame)
            noti_frame.pack(fill="x", padx=10, pady=5)

            # Add circular image
            image = create_circle_image(notification["image"], 50)
            img_label = tk.Label(noti_frame, image=image)
            img_label.image = image
            img_label.pack(side="left", padx=5)

            # Add notification text
            button = ttk.Button(
                noti_frame,
                text=f"{notification['club']} - 더보기",
                command=lambda n=notification: self.open_detail_window(
                    n["club"], n["text"]
                ),
            )
            button.pack(side="left", padx=10)

    def create_resource_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="동아리 자료실")

        scrollable_frame = self.create_scrollable_canvas(frame)

        for resource in resources:
            res_frame = ttk.Frame(scrollable_frame)
            res_frame.pack(fill="x", padx=10, pady=5)

            # Add resource type and title
            button = ttk.Button(
                res_frame,
                text=f"{resource['type']} - {resource['title']}",
                command=lambda r=resource: self.open_detail_window(
                    r["type"], r["title"]
                ),
            )
            button.pack(side="left", padx=5)

        # Upload section
        upload_frame = ttk.Frame(scrollable_frame)
        upload_frame.pack(fill="x", pady=20)

        title_label = tk.Label(upload_frame, text="자료 제목", font=("Arial", 12))
        title_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        title_entry = ttk.Entry(upload_frame, width=20)
        title_entry.grid(row=0, column=1, padx=10, pady=5)

        content_label = tk.Label(upload_frame, text="자료 내용", font=("Arial", 12))
        content_label.grid(row=1, column=0, padx=10, pady=5, sticky="nw")
        content_entry = tk.Text(upload_frame, width=20, height=5)
        content_entry.grid(row=1, column=1, padx=10, pady=5)

        upload_button = ttk.Button(
            upload_frame,
            text="등록하기",
            command=lambda: self.open_detail_window(
                "등록 확인", f"'{title_entry.get()}' 자료가 등록되었습니다!"
            ),
        )
        upload_button.grid(row=2, column=1, pady=10, sticky="e")

    def create_mypage_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="마이페이지")

        scrollable_frame = self.create_scrollable_canvas(frame)

        for section, club_list in clubs.items():
            section_label = tk.Label(
                scrollable_frame, text=section, font=("Arial", 16, "bold"), anchor="w"
            )
            section_label.pack(fill="x", padx=10, pady=5)

            for club in club_list:
                club_frame = ttk.Frame(scrollable_frame)
                club_frame.pack(fill="x", padx=10, pady=5)

                # Add circular image
                image = create_circle_image(club["image"], 50)
                img_label = tk.Label(club_frame, image=image)
                img_label.image = image
                img_label.pack(side="left", padx=5)

                button = ttk.Button(
                    club_frame,
                    text=f"{club['name']} - 더보기",
                    command=lambda c=club: self.open_detail_window(
                        c["name"], f"{c['name']}에 대한 상세 정보"
                    ),
                )
                button.pack(side="left", padx=10)


# Run the application
if __name__ == "__main__":
    app = ClubApp()
    app.mainloop()
'''

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw


# Helper function to create circular images
def create_circle_image(image_path, size):
    try:
        img = Image.open(image_path).resize((size, size), Image.Resampling.LANCZOS)
        circle = Image.new("L", (size, size), 0)
        draw = ImageDraw.Draw(circle)
        draw.ellipse((0, 0, size, size), fill=255)
        img.putalpha(circle)
        return ImageTk.PhotoImage(img)
    except:
        placeholder = Image.new("RGB", (size, size), color="gray")
        return ImageTk.PhotoImage(placeholder)


# Data
notifications = [
    {"club": "그림 동아리", "text": "그림 과제 제출 완료", "image": "art club.jpg", "read": False},
    {"club": "영화 동아리", "text": "이번주 7/23일 모임 공지", "image": "movie club.jpg", "read": False},
    {"club": "코딩 동아리", "text": "새 자료가 등록되었습니다", "image": "coding club.jpg", "read": False},
    {"club": "영어 회화 동아리", "text": "모임 장소 변경 안내", "image": "english club.jpg", "read": False},
    {"club": "발표 동아리", "text": "코멘트가 등록되었습니다\n한글 파일 첨부 hwp", "image": "presentation club.jpg", "read": False},
    {"club": "베이킹 동아리", "text": "활동 사진이 등록되었습니다", "image": "baking club1.jpg", "read": False},
]

resources = [
    {"type": "사진", "title": "2024-07-01 활동 사진", "icon": "photo.jpg"},
    {"type": "동영상", "title": "토론발표 영상\n업로드 | 3일 전", "icon": "video.jpg"},
    {"type": "파일", "title": "2기 코딩 동아리 지원 양식.pdf", "icon": "file.jpg"},
    {"type": "코드 소스", "title": "code.py", "icon": "code.jpg"},
]

clubs = {
    "지원한 동아리": [{"name": "그림 동아리", "image": "art club.jpg"}, {"name": "영화 동아리", "image": "movie club.jpg"}],
    "현재 활동 중인 동아리": [{"name": "코딩 동아리", "image": "coding club.jpg"}, {"name": "영어 회화 동아리", "image": "english club.jpg"}],
    "찜한 동아리": [{"name": "발표 동아리", "image": "presentation club.jpg"}, {"name": "베이킹 동아리", "image": "baking club1.jpg"}],
}


class ClubApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("동아리 앱")
        self.geometry("300x500")

        # Tabs
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)

        # Active Filter
        self.active_club_filter = "전체"

        # Create Tabs
        self.create_notification_tab()
        self.create_resource_tab()
        self.create_mypage_tab()

    def create_scrollable_canvas(self, parent):
        canvas = tk.Canvas(parent)
        scrollbar = ttk.Scrollbar(parent, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all")),
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        return scrollable_frame

    # Notification Tab
    def create_notification_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="동아리 알림")

        self.scrollable_frame = self.create_scrollable_canvas(frame)
        self.update_notification_tab()

    def update_notification_tab(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        for notification in notifications:
            noti_frame = ttk.Frame(self.scrollable_frame)
            noti_frame.pack(fill="x", padx=10, pady=5)

            # Add circular image
            image = create_circle_image(notification["image"], 50)
            img_label = tk.Label(noti_frame, image=image)
            img_label.image = image
            img_label.pack(side="left", padx=5)

            # Add notification button
            button = ttk.Button(
                noti_frame,
                text=f"{notification['club']}",
                command=lambda n=notification: self.open_notification_detail(n),
            )
            button.pack(side="left", padx=10)

            # Add unread indicator
            if not notification["read"]:
                unread_label = tk.Label(noti_frame, text="🔴", fg="red")
                unread_label.pack(side="right", padx=10)

    def open_notification_detail(self, notification):
        notification["read"] = True
        detail_window = tk.Toplevel(self)
        detail_window.title(notification["club"])
        detail_window.geometry("300x300")

        label = tk.Label(detail_window, text=notification["text"], wraplength=280, justify="left")
        label.pack(pady=10)

        close_button = ttk.Button(detail_window, text="닫기", command=detail_window.destroy)
        close_button.pack(pady=10)

        self.update_notification_tab()

    # Resource Tab
    def create_resource_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="동아리 자료실")

        scrollable_frame = self.create_scrollable_canvas(frame)

        for resource in resources:
            res_frame = ttk.Frame(scrollable_frame)
            res_frame.pack(fill="x", padx=10, pady=5)

            icon = create_circle_image(resource["icon"], 50)
            icon_label = tk.Label(res_frame, image=icon)
            icon_label.image = icon
            icon_label.pack(side="left", padx=5)

            button = ttk.Button(
                res_frame,
                text=f"{resource['type']}",
                command=lambda r=resource: self.open_resource_detail(r),
            )
            button.pack(side="left", padx=5)

    def open_resource_detail(self, resource):
        detail_window = tk.Toplevel(self)
        detail_window.title(resource["type"])
        detail_window.geometry("300x300")

        label = tk.Label(detail_window, text=resource["title"], wraplength=280, justify="left")
        label.pack(pady=10)

        close_button = ttk.Button(detail_window, text="닫기", command=detail_window.destroy)
        close_button.pack(pady=10)

    # MyPage Tab
    def create_mypage_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="마이페이지")

        filter_frame = ttk.Frame(frame)
        filter_frame.pack(fill="x", pady=10)

        for filter_name in ["전체", "지원한 동아리", "현재 활동 중인 동아리", "찜한 동아리"]:
            button = ttk.Button(
                filter_frame,
                text=filter_name,
                command=lambda f=filter_name: self.update_mypage_list(f),
            )
            button.pack(side="left", padx=5)

        self.mypage_frame = self.create_scrollable_canvas(frame)
        self.update_mypage_list("전체")

    def update_mypage_list(self, filter_name):
        self.active_club_filter = filter_name

        for widget in self.mypage_frame.winfo_children():
            widget.destroy()

        if filter_name == "전체":
            all_clubs = [club for group in clubs.values() for club in group]
        else:
            all_clubs = clubs.get(filter_name, [])

        for club in all_clubs:
            club_frame = ttk.Frame(self.mypage_frame)
            club_frame.pack(fill="x", padx=10, pady=5)

            image = create_circle_image(club["image"], 50)
            img_label = tk.Label(club_frame, image=image)
            img_label.image = image
            img_label.pack(side="left", padx=5)

            button = ttk.Button(
                club_frame,
                text=club["name"],
                command=lambda c=club: self.open_club_detail(c),
            )
            button.pack(side="left", padx=10)

    def open_club_detail(self, club):
        detail_window = tk.Toplevel(self)
        detail_window.title(club["name"])
        detail_window.geometry("300x300")

        label = tk.Label(detail_window, text=f"{club['name']} 상세 정보")
        label.pack(pady=10)

        close_button = ttk.Button(detail_window, text="닫기", command=detail_window.destroy)
        close_button.pack(pady=10)


if __name__ == "__main__":
    app = ClubApp()
    app.mainloop()
