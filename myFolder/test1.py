from djitellopy import Tello

# 드론 객체 생성
tello = Tello()

# 드론 연결
tello.connect()

# 배터리 잔량 출력
print(f"\n배터리 잔량: {tello.get_battery()}%\n")

# 드론 이륙
tello.takeoff()

# 드론 전진
tello.move_forward(30)

# 드론 좌회전
tello.rotate_counter_clockwise(90)

# while 1:
#     # 키보드 입력 받기
#     key = cv2.waitKey(1) & 0xff
#     if key == 27: # ESC
#         break
#     elif key == ord('w'):
#         tello.move_forward(30)
#     elif key == ord('s'):
#         tello.move_back(30)
#     elif key == ord('a'):
#         tello.move_left(30)
#     elif key == ord('d'):
#         tello.move_right(30)


tello.land()
