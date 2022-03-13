#Development diary

##Decisions made:
1. I chose FastApi + websockets + javascript.
2. I decide to render scene (read from websocket) 30 rps.
3. Let the game screen be 400x400 px.
4. Let the pong racket (or pad) be 80х10 px.
5. Players can't change pad.
6. Let the ball be 10х10 px.
7. Let the control be arrows and kick ball by Enter.
8. I decided to simplify and not calculate the curvature according to the formula, but just figure out how far the hit is from the center of the racket.
9. I decided that for simplicity, the one who last touched the ball gets the point.
10. I decided that after kick ball flies straight.
11. I decided that the farther the ball hits from the center of the racket, the faster the ball flies.
12. I decided to add reset button.


##Plan
1. Start rest api.
2. Try to render scene for one player.
3. Try to send pressed keys.
4. Receive keys and render scene after it.
5. Start virtual machine for testing.
6. Try to render scene for two pads.
7. Adequately maintain the number of entered players.
8. Calculate fly of ball.
9. Calculate collisions. At first for two than for four players.
10. Ball reload.
11. Right score.
12. Calculate speed of ball.
13. Add comments & README

##My thoughts and reflection
1. First thought, you need to go to api 30 times per second and render the scene.
2. For these purposes, restapi is not suitable. Because it will be about 30 * 4 = 120 rps. It will run too slowly.
3. So I need to do on websockets
4. Now I need render.
5. Do not forget about the timestamp from messages (Do I need it?) But actually I try to send message without timestamp, and it works ok.
6. How to store system state? It seems that you can save a lot if you divide the ball and platforms into different channels.
7. I moved the ball flies to a separate render, just to send the state of the system there.
8. It would be nice, of course, to tie everything to the parameters, the size of the pad, the size of the ball, the size of the site.
9. I saw a problem, the number of players, the ball starts to move faster, I need to remove move_ball() from the socket.
As a result, I cheated a little here, and made the speed dependent on the number of connections :). I think this problem can be solved by launching a separate process and, for example, key-value cache, but I did not have time to make such a design.
10. A couple of bugs need to be fixed related to reloading / exiting a player with an attached ball
11. I'm starting to think what needs to be rolled out to a virtual machine and start making out a readme.
12. I also tested it on a virtual machine, I need to fix the endless loop ConnectionClosedError.
