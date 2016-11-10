#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
#perCentQueueUtilization_levels


register_check_parameters(
    subgroup_networking,
    "asyncos_queue",
    _("AsyncOS Queue"),
    Dictionary(
        elements = [
            ("perCentQueueUtilization_levels", Tuple(
                title = _("Levels for Queue Utilization"),
                elements = [
                    Percentage(title = _("Warning at a value of"), default_value=70.0),
                    Percentage(title = _("Critical at a value of"), default_value=85.0)
                  ],
                ),
            ),
			("queueAvailabilityStatus_levels", Tuple(
					title = _("Levels for availability status"),
					elements = [
						DropdownChoice(
							title = ("Warn on status"),
							default_value = 2,
							choices = [
								( 3,  _("Full") ),
								( 2,  _("Shortage") ),
								( 1,  _("Available") ),
							]
						),
						DropdownChoice(
							title = ("Crit on status"),
							default_value = 3,
							choices = [
								( 3,  _("Full") ),
								( 2,  _("Shortage") ),
								( 1,  _("Available") ),
							]
						),
					],
				),
			),
			("workQueueMessages_levels", Tuple(
                title = _("Levels for work queue"),
                elements = [
                    Integer(title = _("Warning at a value of"), default_value=9999),
                    Integer(title = _("Critical at a value of"), default_value=1000000)
                  ],
                ),
            ),
        ]
    ),
    TextAscii(
        title = _("Name of the queue"),
    ),
    "dict"
)
