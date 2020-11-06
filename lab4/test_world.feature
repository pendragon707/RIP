Feature: World
	A place where you can breed bacteria and mushrooms

	Scenario: Creating the world
		Given nature and builder

		Then The world should be created

		When Create four cells

		Then ok

		When Cells lives

		Then Cells should dies
