total_cnt = 100
fail_cnt = 20

success_cnt = total_cnt - fail_cnt
success_rate = success_cnt / total_cnt * 100

print("===== 데이터 검증 테스트 =====")
print("전체 건수:", total_cnt)
print("실패 건수:", fail_cnt)
print("성공 건수:", success_cnt)
print("성공률: {:.1f}%".format(success_rate))
