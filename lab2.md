    Lab 3

[![](./Lab 3_files/favicon270circle.png)](https://engineering.purdue.edu/ece270/)

[

About

](https://engineering.purdue.edu/ece270/about)[

Labs

](https://engineering.purdue.edu/ece270/lab)[

Notes

](https://engineering.purdue.edu/ece270/notes)[

References

](https://engineering.purdue.edu/ece270/refs)

* * *

Lab 3
=====

Measurement of Electrical and Timing Characteristics of Logic Gates
===================================================================

* * *

Table of Contents
-----------------

  

Step

Description

Points

0

Prelab

25

1

Inverter Threshold Voltage Measurements

12

2

Schmitt Inverter Voltage Threshold Measurements

12

3

Circuit Construction and Test

20

4

Propagation Delay Measurements

31

5

Confirm checkoffs and clean up

0\*

 

Total:

100

document.querySelector("table").classList.add("toc");  

\* 25% penalty for late checkoffs, late postlab, bringing in liquids, or leaving an unclean/unusable station.

Instructional Objectives
------------------------

*   To exercise construction techniques by constructing a complex circuit to achieve a useful purpose.
*   To learn the purpose of electronic measurement devices like multimeters and oscilloscopes.
*   To learn how to use those devices.
*   To learn how to measure logic signal propagation times using an oscilloscope.

Introduction
------------

**For this lab, you will need your lab kit, the extra digital chips, and an AD2. Please read the entire document to determine what chips you may need, if any, and use them to complete circuit construction before your lab section.**  
You will construct an adder circuit that can be used to take two numbers as an input, and add them to produce a result. In addition, this lab will focus on calculating the propagation delay of individual gates, as well as the delay between first input and the change in output.

**The construction for this lab cannot be completed within the lab section in sufficient time.** This is a long lab, and if you do not have your circuit built prior to your lab section you will not be able to finish in time to receive all your checkoffs. Please build the circuit and verify your construction using Autolab prior to your lab section.

At the beginning of this lab, as well as each one going forward, **rerun the setup script on your lab machine**. Try to make it a habit.

Step 0: Prelab
--------------

*   Do the [prelab assignment](https://engineering.purdue.edu/ece270/submit/?item=prelab3) on the course web page.
*   Read this entire lab document so you can anticipate how long it will take to complete.
*   **Build the circuits in Steps 1+2, and 3 (1 and 2 share circuits.)** Please make sure to do this before your lab section.

Step 1: Inverter Threshold Voltage Measurements
-----------------------------------------------

In this experiment, you will determine your 74HC04 inverter's transition voltage thresholds (VT- and VT+). When the input voltage crosses this transition point (crossing either from high-to-low or low-to-high), the inverter will switch outputs accordingly.  
  
To do so, use the waveform generator of the AD2 to set up a sine wave to use as an input to an inverter. Use the two-channel oscilloscope to view both the input and the output of the inverter. When the inverter output switches from high to low, you know that the input has reached the VT+ threshold to recognize it as a "high". When the inverter output switches from low to high, you know that the input has reached the VT- threshold to recognize it as a low.

### Procedure

It is also possible to do this portion of the lab at home as well, using the oscilloscope function on your AD2 in place of a lab oscilloscope. Use the special instructions for AD2s instead of the ones for the oscilloscope wherever you see them. (If you are using the oscilloscope in lab, you do not have to do the instruction portion relating to the AD2 scope.) However, for full points, you must still attend your lab section and demonstrate it on the lab oscilloscope for better precision.

Follow these steps to obtain your threshold voltage measurements:

1.  Wire a 74HC04 inverter chip on your breadboard. Be sure to connect the power and ground pins to the appropriate buses. If you want to, you may connect the AD2 V+ and one of the Ground pins directly to the integrated circuit.
    
2.  Invoke the WaveForms application and associate it with the AD2 system. In the "Welcome" menu, select the "Supplies". Select a supply voltage of 3.3 V, and **enable** the output.
    
3.  Invoke the "Wavegen" tool in the WaveForms "Welcome" menu. Configure it as follows:
    
    *   Type: **Sine** (Feel free to use Triangle instead)
    *   Frequency: 1 kHz
    *   Period: 1 ms
    *   Amplitude: 1 V
    *   Offset: 1 V
    *   Symmetry: 50 %
    *   Phase: 0°

**And press the "Run" button to make it start.**

The result should be a wave that varies from 0V to 2V. The 1 kHz frequency is slow enough that the propagation delay for the inverter is _(negligible)_ compared to the wave change. This means that if you view the input and output on top of each other, the point at which the output transitions will be very close in time to the point where the input threshold is reached which caused the output transition. (In other words, if you used a high frequency input, there would be a visible delay on the scope between the input level that caused a transition and the output transition. Slow is good for this measurement.)

*   Connect the W1 pin of the AD2 to the input of one of the six inverters of the 74HC04.
    
*   Connect probe 1 on the MSOX-3014A oscilloscope on your bench to the chosen input pin on your the inverter. Connect the probe itself to the input pin, and the black alligator clip to ground.
    
    *   If you're using your AD2, connect the 1+ line of the AD2 to the input of the selected inverter. **Be sure to also connect the 1- line of the AD2 to ground.**
*   Connect probe 2 on the MSOX-3014A oscilloscope on your bench to the corresponding output pin on your the inverter. Connect the probe itself to the output pin, and the black alligator clip to ground.
    
    *   If you're using your AD2, connect the 2+ line of the AD2 to the output of the selected inverter. **Be sure to also connect the 2- line of the AD2 to ground.**
*   Press the Auto Scale button to get a clear view of the sine wave on your input pin probe, and the resulting square wave on your output pin probe.
    
    *   If you're using your AD2, invoke the "Scope" tool in the WaveForms "Welcome" menu. Configure it as follows:
        *   Set the Channel 1 and Channel 2 controls on the right side to **Offset: -1 V** and **Range: 200 mV/div**. This will center the input and output waveforms on the screen.
        *   In the bar above the scope display, change it from "Auto" to "Normal" trigger mode. **Source: Channel 1**. **Condition: Rising**. **Level 1V**.
        *   Press the "Run" button.

The result should look something like the following (this applies if you're on an AD2 as well):

![If this diagram didn't appear, contact course staff.](./Lab 3_files/inverter-graph-2.png)

Figure 1: 74HC04 Transition Voltage Demonstration

The yellow trace is Probe 1 (inverter input), and the green trace is Probe 2 (inverter output). Be sure you are able to see a full cycle of the input and output waveforms. You may adjust the scope using the Vertical and Horizontal knobs to get more or less of the waveforms in view.

Now, press the Cursors button on your oscilloscope. Adjust the X and Y cursor such that the X cursors coincide with where the green output waveform falls and rises, and the Y cursors to where the placement of the X cursors coincides with the input waveform.

*   If you're using the AD2, turn on the "X Cursors" and "Y Cursors" to aid in evaluating the time difference between the two rising edges.

It should look like the following:

![If this diagram didn't appear, contact course staff.](./Lab 3_files/inverter-graph-2-2.png)

Figure 2: 74HC04 Transition Voltage Demonstration with measurement cursors

### A note on observations

Every inverter is different! No inverter is perfect! Your display should look vaguely like the one shown above, but it need not be exactly the same.

Read the long note about the [counterfeit inverters](https://engineering.purdue.edu/ece270/refs/counterfeit/). If you have one of these inverters, you will see a slightly different pattern. **This is not a bad thing.** Even though the inverters are counterfeit, they still work well as digital inverters. You only see unexpected results because they're being subjected to slowly-changing analog levels.

### Step deliverables

Once you have a scope view **similar to the second picture**, take note of the Y1 and Y2 readings on the bottom right of your scope - these are the VT+ and VT- attributes for your 74HC04. Take a screenshot of the scope using the Scopeshot program, and submit it, along with the transition voltage values, to the [postlab submission page](https://engineering.purdue.edu/ece270/submit/?item=postlab3). **Show your TA your running scope to receive credit for this step.**

Step 2: Schmitt Inverter Voltage Threshold Measurements
-------------------------------------------------------

In a real circuit, the closeness of the two transition points of the inverter would be problematic while dealing with input voltages that may fluctuate across these two close points. The Schmitt trigger is a special comparator circuit that overcomes this problem by effectively "cleaning" such noisy analog signals and converting it into a clean digital one, as the nature of this inverter causes the two transition points to be further away from each other, requiring low-to-high and high-to-low transitions on the input signal to be more pronounced if the output is to change.

### Measurement Procedure

The easiest way to obtain the measurements for Step 2 is to remove the 74HC04 inverter and replace it with a 74HC14 Schmitt-trigger inverter. The resulting graph should look similar to the one pictured below.

![If this diagram didn't appear, contact course staff.](./Lab 3_files/schmitt-graph-2.png)

Figure 3: 74HC14 Transition Voltage Demonstration

The yellow trace is Probe 1 (inverter input), and the green trace is Probe 2 (inverter output). Be sure you are able to see a full cycle of the input and output waveforms. You may adjust the scope using the Vertical and Horizontal knobs to get more or less of the waveforms in view.

Using the same instructions as the last step, set up the cursors in order to get the transition voltages for the 74HC14 gate now. It should look somewhat like the following:

![If this diagram didn't appear, contact course staff.](./Lab 3_files/schmitt-graph-2-2.png)

Figure 4: 74HC14 Transition Voltage Demonstration with measurement cursors

### Step deliverables

Once you have a scope view **similar to the second picture**, take note of the Y1 and Y2 readings on the bottom right of your scope - these are the VT+ and VT- attributes for your 74HC14. Review the lecture notes to remember which is which. Take a screenshot of the scope using the Scopeshot program, and submit it, along with the transition voltage values, to the [postlab submission page](https://engineering.purdue.edu/ece270/submit/?item=postlab3). **Show your TA your running scope to receive credit for this step.**

Step 3: Circuit Construction and Test
-------------------------------------

For this step, you will construct a digital system known as an _adder_. It adds two binary numbers to produce a binary sum. It is one of the most common combinational circuits, and we will study it in detail in module 4. It is not necessary to fully understand the operation of this system, although it not to difficult to do so if you want to. We use this system for two reasons:

*   It has a well-defined set of inputs and outputs. This allows construction to be verified correct in a straightforward manner.
    
*   It has a long path of gates so that a change in a single input will have to propagate through multiple gates, in sequence, before it affects an output. This creates a long _(path delay)_ that allows us to appreciate the total amount of delay in the circuit as a result of many gates connected in series.
    

The kind of adder built is a two-bit adder. It accepts an input of two two-bit binary numbers, as well as a _(carry-in)_ and produces a three-bit binary result. A two-bit binary adder can be constructed from two one-bit _(full adders)_.

### The Full Adder

A full adder accepts two one-bit binary inputs, as well as a _(carry-in)_ and produces a one-bit sum and a _(carry-out)_. The carry-out can be thought as the upper bit of a two-bit sum. If the all three of the inputs are one, then the decimal sum of those bits should be 3. This is represented as a binary 11. This binary sum can be represented with two bits.

The truth table for the two outputs of the full adder can be easily derived using knowledge of conventional addition. In the table below, A and B are the one-bit binary inputs. Cin is the carry-in. All three of these inputs are _(summed)_ together to produce the decimal sum. The binary representation of the decimal sum is represented by Cout and S.

For instance, if the A, B, Cin inputs are 1,0,1, the number of 1-bits in the input is 2. The binary representation of 2 is 10, so Cout=1 and S=0.

A

B

Cin

Sum

Cout

S

0

0

0

0

0

0

0

0

1

1

0

1

0

1

0

1

0

1

0

1

1

2

1

0

1

0

0

1

0

1

1

0

1

2

1

0

1

1

0

2

1

0

1

1

1

3

1

1

The Boolean functions for this truth table is realized by the following circuit:

![If this diagram didn't appear, contact course staff.](./Lab 3_files/transform-and-or.png)

Figure 5: Full Adder Schematic

Again, you are not expected to understand the derivation of this circuit. You may visually inspect it to make sure that it realizes the functions shown by the truth tables.

### Applying DeMorgan's Law

You may notice that the full adder has two XOR gates, two AND gates, and an OR gate. There is, however, no OR gate in your parts kit. This is an excellent opportunity to demonstrate an application of DeMorgan's Law. Let's take only the AND-OR portion of the full adder and transform it.

We can add inversion bubbles to each side of the AND-OR connection. When we do so we have NAND gates, and an OR gate with inverted inputs. DeMorgan's Law tells us that

  X' + Y' == (X · Y)'

so an OR gate with two inverted inputs is _(equivalent)_ to a NAND gate. The leftmost figure of the diagram, above, shows the final result of the DeMorgan's Law transform. An AND-OR tree can always be transformed into a NAND-NAND tree. This is a helpful thing to realize, and it will be useful in future exercises.

### Chaining adders

Typically, multiple one-bit full adders can be _(chained)_ together two form a multi-bit adder. This is done by dividing the binary addition into the 1's place, the 2's place, the 4's place, the 8's place, and so on for as many powers of two as needed. The carry-out from the 1's place is used as the carry-in for the 2's place. The carry-out from the 2's place is used as the carry-in for the 4's place.  
A two-bit adder would be chained as shown below.

![If this diagram didn't appear, contact course staff.](./Lab 3_files/two-bit-adder.png)

Figure 6: AND/OR/XOR implementation of Full Adder

And, of course, we could replace the AND-OR tree with a NAND-NAND tree to form a circuit that can be built with the components in your digital parts kit.

![If this diagram didn't appear, contact course staff.](./Lab 3_files/two-bit-nand-adder.png)

Figure 7: NAND/XOR implementation of Full Adder

**The full schematic of the circuit to build for this lab is shown below.** Four buttons are used to provide the two two-bit inputs A1, A0 and B1,B0. The inputs are naturally in the "low" state unless a button is pressed to set them to the "high" state. The carry-in is held low by a pull-down resistor (you must use 10K ohm resistors). Points are labeled where the AD2 will be connected.

![If this diagram didn't appear, contact course staff.](./Lab 3_files/full-schematic.png)

Figure 8: Full Schematic

At first glance at this schematic, it may look like this could take a very long time to assemble. All that is required is some planning and guidelines for where to put things to make the implementation as quick and convenient as possible. You are welcome (and encouraged) to do your own implementation. Otherwise, you may follow the step-by-step instructions below.

### Insert chips and push buttons

Insert the chips and push buttons in the order and placement shown below. Note the hole numbers on the breadboard. You may use these numbers as a guide. The chips are places precisely so that wires can be inserted between them. Add the 10k pull-down resistors to the push buttons in the locations shown. Finally, connect each chip and push button to the power and ground buses. (All the ground buses are connected together and all the power buses are connected together on the other side of the board.)

![If this diagram didn't appear, contact course staff.](./Lab 3_files/place-chips.jpg)

Figure 9: Chip Placement

### Wire full adder "0"

Next, wire full adder "0". It will done entirely on the lower side of the chips. Your wire kit contains lengths of wires that are identifiable by color. Choose the right color, and you have the right length of wire. If you find the precise hole to place one end of the wire, the other end will naturally fit into the other appropriate spot. The A0 button on the right is connected by the gray wire to the A input of the XOR gate. The B0 button on the left is connected by the purple wire to the B input of the NAND gate. The A and B inputs of the NAND gate and XOR gate are connected together by the white wires. In this way, the A and B connections easily span the adder.

Add two LEDs with series 150 Ω resistors. Let the green one represent S0 (the least significant bit of the sum — AKA the one's place). Let the yellow LED represent Cout0, the intermediate carry result. You can use this to test that the carry out of adder "0" is working correctly.

Use the shortest wires possible so that the wires lay flat to the breadboard, as shown in the picture. You should not have longer wires creating arches above the surface of the breadboard.

Finally, notice that the new 10KΩ resistor in the center. It is connected to the Cin0 input of the AND gate. The Cin0 is connected to the Cin0 input of the XOR gate by the gray wire that runs between them.

![If this diagram didn't appear, contact course staff.](./Lab 3_files/place-adder0.jpg)

Figure 10: Full Adder 0

You are expected to use the datasheets for each IC to build your circuit. Do not try to copy and paste the example wiring or you will run into issues. The figure underneath should be used for reference only. Click/tap to continue.

function toggleOverlay(btn) { btn.parentElement.style\['z-index'\] = '-1'; btn.parentElement.style.opacity = '0'; btn.parentElement.children\[0\].style.display = 'none'; }

### Test full adder "0"

Don't wire anything else yet. Apply a 4.5V power supply, and test this circuit with the B0 and A0 push buttons.

*   If neither B0 nor A0 are pressed, no LEDs are illuminated. This represents the sum zero.
    
*   If either one of B0 or A0 are pressed (but not both), the green LED should illuminate. This represents the sum one.
    
*   If both B0 and A0 are pressed, the yellow LED should illuminate. This represents the sum two.
    
*   You might temporarily connect the Cin0 input to power either by running a wire to it or moving the other terminal of the resistor to the power bus. Upon doing so, the sums should be one higher than they were for the cases above. When both buttons are pressed, both LEDs should illuminate to represent the sum three. (Remember to restore Cin0 so that no LEDs are lit when no buttons are pressed.)
    

### Wire full adder "1"

Wire adder "1" on the "upper" side of the chips exactly as the bottom side, but slide each wire to the right by one hole as shown in the figure below. (Remember that the logic gates on the "upper" side are one position to the left of the gates on the "lower" side.)

![If this diagram didn't appear, contact course staff.](./Lab 3_files/place-adder1.jpg)

Figure 11: Full Adder 1

You are expected to use the datasheets for each IC to build your circuit. Do not try to copy and paste the example wiring or you will run into issues. The figure underneath should be used for reference only. Click/tap to continue.

function toggleOverlay(btn) { btn.parentElement.style\['z-index'\] = '-1'; btn.parentElement.style.opacity = '0'; btn.parentElement.children\[0\].style.display = 'none'; }

### Test full adder "1"

Add the LEDs for S1 and S2 (Cout1) to the upper adder as shown in the picture below. The LEDs, from left to right represent Cout0 (yellow), S2, S1, and S0. You should be able to read the full sum by looking at the binary pattern on S2,S1,S0 and it should represent the addition of the inputs.

Connect buttons B1 and A0 to their inputs with long green and orange wires. It may help to bend corners into the wires to keep them from looping around your breadboard.

Apply 4.5V to the system, and test it thoroughly. If you press all four buttons (which represents a three on each input), you should see the green LEDs show the binary pattern 1 1 0, which represents the decimal quantity six. If you temporarily connect the Cin0 input to power, it will add one more of any of the combinations you try. With all buttons pressed (3 + 3) and Cin0 pulled high (+1) the end result should be all three green LEDs illuminated (a sum of 7).

![If this diagram didn't appear, contact course staff.](./Lab 3_files/place-leds.jpg)

![If this diagram didn't appear, contact course staff.](./Lab 3_files/full-schematic.png)

Figure 12: Full Adder 1 Test

You are expected to use the datasheets for each IC to build your circuit. Do not try to copy and paste the example wiring or you will run into issues. The figures underneath should be used for reference only. Click/tap to continue.

function toggleOverlay(btn) { btn.parentElement.style\['z-index'\] = '-1'; btn.parentElement.style.opacity = '0'; btn.parentElement.children\[0\].style.display = 'none'; }

### Chain adder "0" to "1"

Notice that, instead of adding a pull-down resistor to the Cin input of the adder "1", a crooked wire connects Cout0 of the lower adder to Cin1 of the upper adder. This chains the adders together. For reference, your circuit should now match the schematic above.

### Test integrated 2-bit adder with 2 full adders

Now, you're ready to test your 2-bit adder! Using the table below, press the buttons to assert an input combination, and ensure that the LEDs reflect the correct output combinations. (Table provided below again for convenience.)



### Verify your circuit with WaveForms StaticIO

Before you use AutoLab to verify your circuit, make it a habit to check your circuit's functionality using the StaticIO panel on WaveForms first. Since AutoLab and WaveForms use the same API to talk to your AD2, they should have the same results. You'll use StaticIO to change inputs to the circuit, and see what the outputs are. This ensures consistency of the circuit with different input methods.

First, connect the AD2 according to the following table:

AD2 pin

Adder

DIO 0

A0

DIO 1

A1

DIO 2

B0

DIO 3

B1

DIO 4

Cin0

DIO 8

S0

DIO 9

S1

DIO 10

S2

DIO 11

Cout0

**Do not remove these connections - you'll need them for AutoLab as well.**

Make sure WaveForms is still open, with the power supplies turned on, and open the StaticIO panel. You should see two rows of 8 LEDs, numbered 15 through 0. These correspond to each of the DIO pins on the AD2.

Click on the DIO numbers that are associated with circuit inputs (A0, A1, B0, B1, Cin0) and change them to be Switches > Push/Pull. This allows you to set a value on those DIO pins without having to hold down a button.

![If this diagram didn't appear, contact course staff.](./Lab 3_files/staticio.png)

Figure 13: StaticIO on WaveForms

Now, use the table of expected results from above to change the switch values such that the corresponding output DIO pins (which should remain LEDs) turn on or off accordingly. For example, setting both A0 and B0 to 1 with the other pins at 0 should set S2 to 0, S1 to 1, S0 to 0 and Cout0 to 1. If there's a mistake, use the schematic to guide you backwards from the pin where the mistake occurred.

### Verify your circuit with Autolab

Since you will be constructing your circuit at home, we will provide an option to use AutoLab on your personal computer. If you don't already have it, download the application [here](https://engineering.purdue.edu/ece270/lab/autolab/). **Please read the instructions carefully in order to make AutoLab work on your computer.**

**Before you run AutoLab, close WaveForms first!**

Once you have manually checked your circuit with WaveForms, we'll use AutoLab to produce a proof-of-work completion code.

**Download the Lab 3 testbench for Autolab for your specific operating system below:**

Select operating system: Linux macOS Windows Download testbench  

**Make sure that you connect DIO 8 through DIO 11 to the gate outputs rather than the LEDs.** You'll get strange results if you don't.

One solution to make AutoLab work properly is to remove the pushbuttons and resistors to let AutoLab drive the circuit directly. **Do this only if you are sure your circuit is right, that it does the right thing in WaveForms StaticIO, that your resistors are at least 1000 ohms, and that it works with the pushbuttons.**

Turn off WaveForms, invoke AutoLab, download the appropriate lab3.labtest file from above, and run the testbench. It will try all 32 possible inputs and check that the values on the Cout0, S2, S1, and S0 are as expected. If there is a discrepancy, it will report it in the log. If all 32 input combinations produce the expected value on a particular output, you pass the test for that output. The tests are reported near the bottom of the log.

Show that your circuit works with AutoLab to a TA in order to receive credit for this step. Show that your circuit is neatly constructed with appropriate length wires that mimic the pictures shown. Make sure to submit the completion code in your [postlab](https://engineering.purdue.edu/ece270/submit/?item=postlab3).

Step 4: Propagation Delay Measurements
--------------------------------------

Consider a case where only buttons B1 and B0 are pressed. In such a case, only S1 and S0 are illuminated. While they are still pressed, if you press A0, it will cause S1 and S0 to turn off and S2 and Cout0 (yellow) to illuminate instead. This exercises a few long delay paths of the circuit, shown below.

![If this diagram didn't appear, contact course staff.](./Lab 3_files/path-delay.png)

Figure 14: Delay paths

When A0 is pressed, the lights _(appear)_ to all change simultaneously, but the paths taken to change S0, Cout0, S1, and S2 involve transiting different numbers of gates. This means that the change will occur for these outputs at different times. The difference in times is too fast for you to see with your eyes, but not too fast for the AD2.

### Using the pattern generator and logic analyzer

Configure the AD2 to assert B1 and B0 and continually toggle A0 while monitoring each of the affected outputs. To do so, you can set up the "Patterns" tool to assert the inputs and the "Logic" tool to view the result.

Do so as follows:

*   In the WaveForms "Supplies" tool, select a voltage of 4.5 V, and make sure it is enabled.
*   In the WaveForms "Welcome" menu, invoke the "Patterns" tool.
*   In the Patterns tool, add three new signals:
    *   Add signal DIO 2 with Output "OS", Type "Constant", and Parameter1 "1".
    *   Add signal DIO 3 with Output "OS", Type "Constant", and Parameter1 "1".
    *   Add signal DIO 0 with Output "OS", Type "Clock", and Parameter1 "5 Hz".

Press **"Run"** and you should see the LEDs blink.

*   In the WaveForms "Welcome" menu, invoke the "Logic" tool.
*   In the Logic tool, add five new signals:
    *   Add signal DIO 0 (A0), and set the T field to "Rise" so that when the Trigger: is "Normal" and in "Simple" mode at the top of the Logic tool, it will be triggered by the rising edge of DIO 0.
    *   Add signal DIO 11 (Cout0), and set the T field to "X".
    *   Add signal DIO 8 (S0), and set the T field to "X".
    *   Add signal DIO 9 (S1), and set the T field to "X".
    *   Add signal DIO 10 (S2), and set the T field to "X".

Press **"Run"** and you should see five traces.

The order of signals added to the Logic tool is deliberate. You should see a trace that looks similar to the graph below.

![If this diagram didn't appear, contact course staff.](./Lab 3_files/logic-4.5v.png)

Figure 14: Logic tool traces

### What are these slopes in the Logic tool trace?

Recall that the minimum time between samples taken by the AD2 is 10 ns. The slopes presented in the Logic tool trace graph are a fiction. These are shown to demonstrate the uncertainty of the measurements between different points. For instance, a sample was taken that indicated DIO 0 (A0) was low, and in the next sample it was high. Since DIO 0 was the trigger source, the first sample where it was high was regarded a time 0. 20 ns later, a sample of DIO 11 was taken where it was low. Another 10 ns later, the sample for DIO 11 was high. A slope was drawn for DIO 11 between the 20 ns and 30 ns points to indicate that the precise time of transition is unknown. The the S0, S1, and S2 outputs on DIO 8 - 10 transition so close together that their times cannot be distinguished by the AD2. How can the timing differences be observed? The right way would be to purchase a more expensive oscilloscope with a much faster sample rate. For educational purposes, there is a different way to see the timing differences.

### Change the supply voltage

Each tool window in Waveforms has an icon in the upper right to "Dock/Undock Window". Click the icon in the Logic tool to undock it so that it appears in a separate window from the main WaveForms application. Meanwhile, switch to the Supplies tool and _(slide)_ the voltage from 4.5 V down to 2.0 V. The LEDs will be very dim at this point, but you don't need to see them. Watch the traces in the Logic tool as you change the supply voltage. Notice how the transitions get farther apart as the supply voltage decreases. Which transition occurs first: S0 or S1?

### Submission of Logic tool trace

Reduce the size of the undocked Logic tool to be just large enough to see the traces and transitions of DIO 0, 11, 8, 9, and 10. You will be exporting a trace of the logic tool in both image and data format. To export a trace of the Logic tool go to File > Export, or pressing Ctrl+E. Select the Image tab to export an image, save the file, and upload it into your postlab submission. Repeat the previous steps but select the Data tab instead to export the data file, save and upload it into your [postlab submission](https://engineering.purdue.edu/ece270/submit/?item=postlab3).

**Ensure that the time and date and serial number are visible on the exported image, make it a PNG format file, and do not make a screenshot. Also, ensure the CSV format file is exported. You will not receive credit otherwise**. Upload both files to the postlab and answer the relevant questions. **Note: The minimum delay should be measured from the endpoint of the input signal (A0) to the starting point of the output signal (Cout0,S0,S1,S2).The maximum delay should be measured from the starting point of the input signal (A0) to the endpoint of the output signal (Cout0,S0,S1,S2).**

### Measure the path delay

Connect the oscilloscope's probe 1 to the A0 signal, and ensure that its black alligator clip is connected to ground. Connect the the oscilloscope's probe 2 pin to the S2 signal, and ensure that its black alligator clip is also connected to ground.In WaveForms, change the frequency on DIO 0 to 50 kHz, and press Auto Scale on the oscilloscope. The result should look similar to the figure below.

![If this diagram didn't appear, contact course staff.](./Lab 3_files/scope-export-2.png)

Figure 15: Oscilloscope view of 50 kHz signal

Once you have verified that it looks similar, zoom in until you see the delay between the input waveform on A0 and the output waveform on S2. Using the Cursors tool, measure this delay by using the midpoint method as detailed in the lecture notes.It should be similar to the following.

![If this diagram didn't appear, contact course staff.](./Lab 3_files/scope-export-2-2.png)

Figure 16: Propagation delay measurement

Remember that all gates, all wires, all breadboards, and all AD2s are different. Your graph will be too.

Once you have a scope view **similar to the second picture**, measure the propagation delay as explained in the lecture notes. Take a screenshot of the scope using the Scopeshot program, and submit it, along with the propagation delay, to the [postlab submission page](https://engineering.purdue.edu/ece270/submit/?item=postlab3). **Show your TA your measured delay to receive full credit for this step.**

Step 5: Confirm checkoffs and clean up
--------------------------------------

Before leaving, confirm with a TA that you have completed the following steps:

*   You can see that you've been checked off by viewing the lab evaluation page.
*   Clean up your lab section, making sure that you've neatly stored all probes, cleaned up any spare wires, and turned off the light.
*   **Log out of your lab station so that you don't get a logout penalty.**

**Make sure to confirm that you have received all checkoffs on the [Evaluation page](https://engineering.purdue.edu/ece270/submit/?item=lab3) for your lab section before leaving.** You must also confirm that you did not receive a 25% penalty for bringing in liquids, or leaving an unclean/unusable station. If you did, you must resolve the issue with your TA before leaving.

* * *

Questions or comments about the course and/or the content of these webpages should be sent to the [Course Webmaster](mailto:ece270@ecn.purdue.edu). All the materials on this site are intended solely for the use of students enrolled in ECE 270 at the West Lafayette Campus of Purdue University. Downloading, copying, or reproducing any of the copyrighted materials posted on this site (documents or videos) for anything other than educational purposes is forbidden.

  

if (localStorage.darkmode == "true") { document.documentElement.setAttribute("theme", "dark"); window.code\_theme = "vs-dark"; } else { document.documentElement.setAttribute("theme", "light"); window.code\_theme = "vs"; }