from djitellopy import TelloSwarm

swarm = TelloSwarm.fromIps([
    "192.168.178.42",
    "192.168.178.43",
    "192.168.178.44"
])

swarm.connect()
swarm.takeoff()

# run in parallel on all tellos
# Execute simultaneously on all Tellos
swarm.move_up(100)

# run by one tello after the other
# Execute one Tello after another
swarm.sequential(lambda i, tello: tello.move_forward(i * 20 + 20))

# making each tello do something unique in parallel
# Make each Tello execute different operations in parallel
swarm.parallel(lambda i, tello: tello.move_left(i * 100 + 20))

swarm.land()
swarm.end()
