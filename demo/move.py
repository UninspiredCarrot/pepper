import naoqi
from pprint import pprint

myBroker = naoqi.ALBroker("myBroker", "0.0.0.0", 0, "10.1.32.201", 9559)
aln = naoqi.ALProxy("ALNavigation")
auto = naoqi.ALProxy("ALAutonomousLife")
alm = naoqi.ALProxy("ALMotion")

commands = {
	"mv" : ["Move", "Y", "X"],
	"hd" : ["Head", "Yaw", "Pitch"],
	"ls" : ["LShoulder", "Pitch", "Roll"],
	"le" : ["LElbow", "Yaw", "Roll"],
	"hp" : ["Hip", "Roll", "Pitch"],
	"rs" : ["RShoulder", "Pitch", "Roll"],
	"re" : ["RElbow", "Yaw", "Roll"],
	"kn" : ["KneePitch"],
	"lw" : ["LWristYaw"],
	"lh" : ["LHand"],
	"rw" : ["RWristYaw"],
	"rh" : ["RHand"],
	"wb" : ["WheelB"],
	"wl" : ["WheelF", "L", "R"]
}

path = "yellow brick road"

def get_path():
	global path
	return path

def reset():
	rest = {'HeadPitch': -0.3850290775299072,
			'HeadYaw': 0.007669925689697266,
			'HipPitch': -0.018407821655273438,
			'HipRoll': -0.013805866241455078,
			'KneePitch': 0.009203910827636719,
			'LElbowRoll': -0.11351466178894043,
			'LElbowYaw': -1.716524362564087,
			'LHand': 0.6660808324813843,
			'LShoulderPitch': 1.7625439167022705,
			'LShoulderRoll': 0.09357285499572754,
			'LWristYaw': 0.12267804145812988,
			'RElbowRoll': 0.10277676582336426,
			'RElbowYaw': 1.6965827941894531,
			'RHand': 0.6669596433639526,
			'RShoulderPitch': 1.7395341396331787,
			'RShoulderRoll': -0.08743691444396973,
			'RWristYaw': -0.04146003723144531,
			'WheelB': 0.0,
			'WheelFL': 0.0,
			'WheelFR': 0.0}
	for key in rest.keys():
		alm.setAngles(key, rest[key], 0.2)

def disable():
	if auto.getState() != "disabled":
		auto.setState("disabled")
		alm.wakeUp()

def angle_change(name, delta, speed=0.3):
	initial = alm.getAngles(name, True)[0]
	alm.setAngles(name, initial + delta, speed)

def read(instructions, step=0.3):
	command = commands[instructions[:2]]
	name = command[0]
	moves = instructions[2:]
	factor = len(moves)
	if len(command) == 1:
		delta = step*factor
		if "s" in moves:
			delta *= -1

	elif "a" in moves or "d" in moves:
		name += command[1]
		delta = step*factor
		if "d" in moves:
			delta *= -1

	elif "w" in moves or "s" in moves:
		name += command[2]
		delta = step*factor
		if "s" in moves:
			delta *= -1
	print({"name": name, "delta": delta})
	return {"name": name, "delta": delta}

def execute(instructions):
	name = instructions["name"]
	delta = instructions["delta"]

	if name[:4] == "Move":
		x = 0
		y = 0
		if name[-1] == "X":
			x = delta
		elif name[-1] == "Y":
			y = delta
		aln.moveAlong(["Holonomic", ["Line", [x,y]], 0.0, 5.0])

	else:
		angle_change(name, delta)

def list():
	body_joint_names = alm.getBodyNames("Body")
	body_angles = alm.getAngles(body_joint_names, True)
	_dict = {}
	for joint_name, angle in zip(body_joint_names, body_angles):
	    _dict[joint_name] = angle
	return _dict

def main():
	disable()
	while True:
		instructions = raw_input("where?: ")

		if instructions == "q":
			break

		if instructions == "list":
			pprint(list())
			continue

		if instructions == "reset":
			reset()
			continue

		execute(read(instructions))
			
	return 'Done'

if __name__ == '__main__':
	main()