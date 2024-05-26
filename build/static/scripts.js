$(document).ready(function() {
    // Initially show the popup
    $('#welcome-popup').fadeIn();

    // Close the popup
    $('#close-popup').click(function() {
        $('#welcome-popup').fadeOut();
    });

    // Initially hide the table
    $('#table-container').hide();

    // Function to filter the table based on the league type
    function filterTable(leagueType) {
        $('#table-container tbody tr').show(); // Show all rows initially

        if (leagueType === 'champions') {
            $('#table-container tbody tr').filter(function() {
                return $(this).find('td:eq(3)').text() !== 'Yes';
            }).hide();
        } else if (leagueType === 'europa') {
            $('#table-container tbody tr').filter(function() {
                return $(this).find('td:eq(4)').text() !== 'Yes';
            }).hide();
        } else if (leagueType === 'conference') {
            $('#table-container tbody tr').filter(function() {
                return $(this).find('td:eq(5)').text() !== 'Yes';
            }).hide();
        } else if (leagueType === 'relegation') {
            $('#table-container tbody tr').filter(function() {
                return $(this).find('td:eq(6)').text() !== 'Yes';
            }).hide();
        }
    }

    // Show the table with animation when any button is clicked
    $('.btn').click(function() {
        $('#table-container').fadeIn();
        if (this.id === 'show-champions') {
            filterTable('champions');
        } else if (this.id === 'show-europa') {
            filterTable('europa');
        } else if (this.id === 'show-conference') {
            filterTable('conference');
        } else if (this.id === 'show-relegation') {
            filterTable('relegation');
        } else {
            $('#table-container tbody tr').show();
        }
    });

    // Popup functionality
    $('#open-popup').click(function() {
        $('#welcome-popup').css('transform', 'translateX(0)');
    });

    $('#close-popup').click(function() {
        $('#welcome-popup').css('transform', 'translateX(-100%)');
    });

    // Show the popup on page load
    $(window).on('load', function() {
        setTimeout(function() {
            $('#welcome-popup').css('transform', 'translateX(0)');
        }, 1000); // Adjust the delay as needed
    });
});
