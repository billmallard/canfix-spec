.. _Requirements:

General Requirements
====================

_`CFX-GEN-001` A minimum level of functionality must be for a device to be considered
compliant with this specification.  Although only part of this specification is
required to be implemented, if any given part of the specification is implemented,
the device is expected to behave according to the descriptions in this specification.

This section describes the minimum functionality that must be present for a
device to be considered compliant with this specification.  The requirements for
this specification have been deliberately kept to a minimum to make
implementation of this specification as easy as possible.

Each requirement in this chapter carries a stable identifier of the form
``CFX-<section>-<number>``, and an item of a requirement's list adds
``.<item>``.  Identifiers are never renumbered or reused.  A requirement that
is withdrawn keeps its identifier and is marked as withdrawn.


Communication Requirements
--------------------------

_`CFX-COM-001` There are several *Node Specific Messages* that the device must respond to.
They are...

  * _`CFX-COM-001.1` Node Identification
  * _`CFX-COM-001.2` Bit Rate Set
  * _`CFX-COM-001.3` Node ID Set
  * _`CFX-COM-001.4` Disable Parameter
  * _`CFX-COM-001.5` Enable Parameter
  * _`CFX-COM-001.6` Node Report

_`CFX-COM-002` All nodes should respond to the Node Identification command even if the only thing
they return is the specification number.

_`CFX-COM-003` It is not required that a device send any parameters listed by the
specification.  However, the device must respond to both the Disable and Enable
Parameter messages.  If there are no parameters to disable or enable the device
can simply respond with an *Unknown Parameter* error.

_`CFX-COM-004` If a device has no parameters to send it is not required to follow a Node Report
request with any data.

_`CFX-COM-005` Data types and units cannot be substituted.  If parameters are sent by a device
they must match the data types and units given in this document.

_`CFX-COM-006` The device should respond to the broadcast address for all messages where it
is appropriate.

_`CFX-COM-007` Bit rate, node ID number and the parameters that have been enabled or disabled
should be stored in non-volatile memory so that these changes are permanent.

_`CFX-COM-008` A device should send at least one self identifying frame on the CAN bus at least
once every 2 seconds to indicate it's health to the system.  Any frame that
includes the device's node number (whether explicitly or implied) will satisfy
this requirement.  The only message types that do not include the sender's node
number are the two-way channel communication frames, these would NOT satisfy
this requirement.

_`CFX-COM-009` The recommendation is to send a Node Status Information message with the status
word set to 0x0000 to indicate good health once per second.

_`CFX-COM-010` 125 kbps and 250 kbps are the only mandatory bit rates.  125 kbps should be
the default.

Physical Requirements
---------------------

_`CFX-PHY-001` There are really no mandatory physical specifications that must be met.  There
are electrical connectors that are specified and if these types of connectors
are used the signals on the pins must match the descriptions in this
specification.

_`CFX-PHY-002` Good engineering practices should be used in the design of these devices.
A complete description is outside the scope of this document, however here is
a short list of issues to pay attention to.

  * _`CFX-PHY-002.1` Wires should be properly supported
  * _`CFX-PHY-002.2` Mounting should be secure and fasteners should be protected from loosening
    due to vibration
  * _`CFX-PHY-002.3` Connectors should be postively retained.  Friction is not a proper
    retention method.
  * _`CFX-PHY-002.4` Components should be properly cooled
  * _`CFX-PHY-002.5` Materials used for construction should not emit noxious fumes if burned.
    Aluminum is a great choice for enclosures, PVC is a terrible choice.

Electrical Requirements
-----------------------

_`CFX-ELE-001` The device should operate properly with supply voltages between 10 and 32 Volts
DC.

_`CFX-ELE-002` The device should be able to withstand reversed polarity connection to it's
power supply input.  The device does not have to protect against being connected
in reverse for prolonged periods of time.  It is assumed that the installer will
have some proper form of circuit protection installed on the power supply to the
device.  This allows a simple shunt diode to be used for this purpose.  More
sophisticated schemes of protection are recommended but not required.

_`CFX-ELE-003` The device is not required to operate while connected in reverse.  It must
simply survive.  In fact is recommended that the device NOT operate properly
while it's power supply is reversed.  This would cause attention to be given to
the device that it would not recieve if it was opearating normally while
connected in reverse.

_`CFX-ELE-004` Good engineering practices should be used in the design of these devices.
A complete description is outside the scope of this document, however here is
a short list of issues to pay attention to.

  * _`CFX-ELE-004.1` Proper shielding should be employed to prevent radio frequency interfernce
    with other devices in the aircraft, if applicable.
  * _`CFX-ELE-004.2` Good power filtering should be used to prevent conducted noise from affecting
    other devices within the aircraft.  Also proper bypassing of high frequency
    components (i.e. microcontrollers) should also be employed for the same
    reason.
  * _`CFX-ELE-004.3` High quality components should be used when possible.
  * _`CFX-ELE-004.4` The system should be designed in such a way, that faults within the device
    will not cause a fire.
