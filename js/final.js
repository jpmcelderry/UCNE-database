function runSearch(){
	//remove old query info and show the 'searching' indicator
    $('#results').hide();
	$('thead').empty();
    $('tbody').empty();
	$('#searching').text("searching");
	$('#search_progress').show();
	
	//get form terms
	var formTerms = $('#UCNE_search').serialize();
	//console.log("Before AJAX")
	//console.log(formTerms)
	
	$.ajax({
        url: './final.cgi',
        dataType: 'json',
        data: formTerms,
        success: function(data, textStatus, jqXHR) {
			//console.log("After AJAX")
            //console.log(data);
			process(data);
        },
        error: function(jqXHR, textStatus, errorThrown){
            alert("Error: textStatus: (" + textStatus +
                  "), errorThrown: (" + errorThrown + ")");
        }
    });
}

function process( data ) {
	//Sort the JSON depending on the sorting preferences
	 switch($('#sort_by').val()){
		case 'UCNE_name':
			data.matches = sortResults(data.matches, 'name', true);
			break;
		case 'organism':
			data.matches = sortResults(data.matches, 'organism', true);
			break;
		case 'chromosome':
			data.matches = sortResults(data.matches, 'chromosome', true);
			break;
		case 'identity_desc':
			data.matches = sortResults(data.matches, 'identity', false);
			break;
		case 'identity_asc':
			data.matches = sortResults(data.matches, 'identity', true);
			break;
		case 'length_desc':
			data.matches = sortResults(data.matches, 'length', false);
			break;
		case 'length_asc':
			data.matches = sortResults(data.matches, 'length', true);
			break;
	 }
	
	//print header information
    $('#match_count').text( data.match_count + " match(es) found.");
    $('<tr/>', {"id" : "header"} ).appendTo('thead')
	$('<th/>', {"text" : "UCNE id"}).appendTo('#header')
	$('<th/>', {"text" : "UCNE name"}).appendTo('#header')
	$('<th/>', {"text" : "UCRB"}).appendTo('#header')
	$('<th/>', {"text" : "organism"}).appendTo('#header')
	$('<th/>', {"text" : "chromosome"}).appendTo('#header')
	$('<th/>', {"text" : "start"}).appendTo('#header')
	$('<th/>', {"text" : "stop"}).appendTo('#header')
	$('<th/>', {"text" : "length"}).appendTo('#header')
	$('<th/>', {"text" : "identity"}).appendTo('#header')
	
    var next_row_num = 1;
    
	//print query results
    $.each( data.matches, function(i, result) {
        var this_row_id = 'result_row_' + next_row_num++;
    
        $('<tr/>', { "id" : this_row_id } ).appendTo('tbody');
        $('<td/>', { "text" : result.UCNE_id } ).appendTo('#' + this_row_id);
        $('<td/>', { "text" : result.name } ).appendTo('#' + this_row_id);
        $('<td/>', { "text" : result.UCRB } ).appendTo('#' + this_row_id);
        $('<td/>', { "text" : result.organism } ).appendTo('#' + this_row_id);
        $('<td/>', { "text" : result.chromosome } ).appendTo('#' + this_row_id);
		$('<td/>', { "text" : result.chr_start } ).appendTo('#' + this_row_id);
		$('<td/>', { "text" : result.chr_stop } ).appendTo('#' + this_row_id);
		$('<td/>', { "text" : result.length } ).appendTo('#' + this_row_id);
		//if the organism is human, don't report identity
		if (result.organism == 'human'){
			$('<td/>', { "text" : "-----" } ).appendTo('#' + this_row_id); 
		}
		else{
			$('<td/>', { "text" : result.identity } ).appendTo('#' + this_row_id); 
		}
	});	
    
	$('#search_progress').hide();
    $('#results').show();
}

//Adapted from 'Sean the Bean' answer here: https://stackoverflow.com/questions/881510/sorting-json-by-values
function sortResults(data, prop, asc) {
    data.sort(function(a, b) {
        if (asc) {
            return (a[prop] > b[prop]) ? 1 : ((a[prop] < b[prop]) ? -1 : 0);
        } else {
            return (b[prop] > a[prop]) ? 1 : ((b[prop] < a[prop]) ? -1 : 0);
        }
    });
    return data;
}

$(document).ready( function() {
  $('#UCNE_name').autocomplete({
	minLength:2,
	dataType: 'json',
	source: "./name_autocomplete.cgi"
    });
	
  $('#UCRB').autocomplete({
	minLength:2,
	dataType: 'json',
	source: "./UCRB_autocomplete.cgi"
    });
	
  /*$('#chromosome').autocomplete({
	minLength:2,
	dataType: 'json',
	source: "./chr_autocomplete.cgi"
    });*/

  $('#submit').click( function() {
        runSearch();
        return false;
    });
})