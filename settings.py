#-*-coding:GBK -*-
class Settings():
	"""���桶���������֡����������õ���"""
	
	def __init__(self):
		"""��ʼ����Ϸ������"""
		# ��Ļ����
		self.screen_width = 900
		self.screen_height = 600
		self.bg_color = (230, 230, 230)
		
		#�ɴ�����
		self.ship_speed_factor = 1.5
		self.ship_limit = 3
		
		#�ӵ�����
		self.bullet_speed_factor = 3
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 3
		
		#����������
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		# fleet_direction Ϊ1��ʾ�����ƶ���Ϊ-1��ʾ������
		self.fleet_direction = 1