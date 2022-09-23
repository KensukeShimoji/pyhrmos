""" 日次勤怠データ """

from dataclasses import dataclass
from typing import Optional


@dataclass
class WorkOutputs:  # pylint: disable=too-many-instance-attributes
    """ 日次勤怠データ """

    user_id: int
    """ ユーザーID """
    number: Optional[str]
    """ 社員番号 """
    full_name: Optional[str]
    """ 氏名 """
    month: Optional[str]
    """ 年月(形式: yyyyMM) """
    day: str
    """ 日付(形式: yyyyMMdd) """
    wday: Optional[str]
    """ 曜日 """
    segment_display_title: Optional[str]
    """ 表示名 """
    segment_title: Optional[str]
    """ 勤務区分 """
    start_at: Optional[str]
    """ 出勤時刻 """
    stamping_start_at: Optional[str]
    """ 出勤時刻(打刻) """
    end_at: Optional[str]
    """ 退勤時刻 """
    stamping_end_at: Optional[str]
    """ 退勤時刻(打刻) """
    break_1_start_at: Optional[str]
    """ 休憩1開始 """
    stamping_break_1_start_at: Optional[str]
    """ 休憩1開始(打刻) """
    break_1_end_at: Optional[str]
    """ 休憩1終了 """
    stamping_break_1_end_at: Optional[str]
    """ 休憩1終了(打刻) """
    break_2_start_at: Optional[str]
    """ 休憩2開始 """
    stamping_break_2_start_at: Optional[str]
    """ 休憩2開始(打刻) """
    break_2_end_at: Optional[str]
    """ 休憩2終了 """
    stamping_break_2_end_at: Optional[str]
    """ 休憩2終了(打刻) """
    procedure_overtime_end_at: Optional[str]
    """ 残業上限時刻 """
    total_break_time: Optional[str]
    """ 休憩時間 """
    time_paid_holiday: Optional[str]
    """ 時間有休 """
    total_over_work_time: Optional[str]
    """ 残業時間 """
    total_over_work_time_36: Optional[str]
    """ 残業時間:36 """
    total_working_hours: Optional[str]
    """ 総労働時間 """
    actual_working_hours: Optional[str]
    """ 実働時間 """
    hours_in_prescribed_working_hours: Optional[str]
    """ 所定内労働 """
    hours_in_statutory_working_hours: Optional[str]
    """ 法定内時間外労働 """
    excess_of_statutory_working_hours: Optional[str]
    """ 法定時間外労働 """
    excess_of_statutory_working_hours_in_holidays: Optional[str]
    """ 法定外休日労働 """
    hours_in_statutory_working_hours_in_holidays: Optional[str]
    """ 法定休日労働 """
    late_night_overtime_working_hours: Optional[str]
    """ 深夜労働 """
    status: Optional[int]
    """ ステータス（1. 未申請, 2. 承認待ち, 3. 承認済み, 4. 再申請(差し戻し)） """
    expense: Optional[int]
    """ 経費 """
    created_at: Optional[str]
    """ 作成日時 """
    updated_at: Optional[str]
    """ 更新日時 """

    @classmethod
    def of(cls, data: dict) -> 'WorkOutputs':  # pylint: disable=invalid-name
        """ factory method.

        Args:
            data (dict): _description_

        Returns:
            WorkOutputs: _description_
        """
        return WorkOutputs(
            user_id=data['user_id'],
            number=data['number'],
            full_name=data['full_name'],
            month=data['month'],
            day=data['day'],
            wday=data['wday'],
            segment_display_title=data['segment_display_title'],
            segment_title=data['segment_title'],
            start_at=data['start_at'],
            stamping_start_at=data['stamping_start_at'],
            end_at=data['end_at'],
            stamping_end_at=data['stamping_end_at'],
            break_1_start_at=data['break_1_start_at'],
            stamping_break_1_start_at=data['stamping_break_1_start_at'],
            break_1_end_at=data['break_1_end_at'],
            stamping_break_1_end_at=data['stamping_break_1_end_at'],
            break_2_start_at=data['break_2_start_at'],
            stamping_break_2_start_at=data['stamping_break_2_start_at'],
            break_2_end_at=data['break_2_end_at'],
            stamping_break_2_end_at=data['stamping_break_2_end_at'],
            procedure_overtime_end_at=data['procedure_overtime_end_at'],
            total_break_time=data['total_break_time'],
            time_paid_holiday=data['time_paid_holiday'],
            total_over_work_time=data['total_over_work_time'],
            total_over_work_time_36=data['total_over_work_time_36'],
            total_working_hours=data['total_working_hours'],
            actual_working_hours=data['actual_working_hours'],
            hours_in_prescribed_working_hours=data['hours_in_prescribed_working_hours'],
            hours_in_statutory_working_hours=data['hours_in_statutory_working_hours'],
            excess_of_statutory_working_hours=data['excess_of_statutory_working_hours'],
            excess_of_statutory_working_hours_in_holidays=data[
                'excess_of_statutory_working_hours_in_holidays'],
            hours_in_statutory_working_hours_in_holidays=data[
                'hours_in_statutory_working_hours_in_holidays'],
            late_night_overtime_working_hours=data['late_night_overtime_working_hours'],
            status=data['status'],
            expense=data['expense'],
            created_at=data['created_at'],
            updated_at=data['updated_at']
        )
