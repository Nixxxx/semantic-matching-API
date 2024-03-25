async function findMatches() {
    console.log("findMatches function called");  // This line of code will be executed when the function is called
    const inputText = document.getElementById('inputText').value;
    const responseData = await fetch('/match', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: inputText, // Use the JSON string directly from the text box
    }).then(response => response.json());

    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = ''; // Clear old results

    // Check whether the returned data is empty or a specific value
    if (!responseData.output_segment || responseData.output_segment.length === 0) {
        // If the returned document is empty
        resultsDiv.innerHTML = 'It is empty';
    }  else {
        responseData.output_segment.forEach(segment => {
        // Create a new div to display segment information
            const segmentDiv = document.createElement('div');
            
            // First display the segment ID and description in this div
            const segmentInfo = document.createElement('p');
            segmentInfo.innerHTML = `<strong>Segment ID: ${segment.segment_id}</strong><br>Description: ${segment.description}`;
            segmentDiv.appendChild(segmentInfo);
            
            // Then display the corresponding candidates in the same div
            segment.candidates.forEach(candidate => {
                const candidateInfo = document.createElement('p');
                candidateInfo.innerHTML = `Candidate ID: ${candidate.candidate_id}, Description: ${candidate.candidate_descriptionAndName}, Similarity: ${candidate.similarity}`;
                segmentDiv.appendChild(candidateInfo);
            });
            
            // Add this segment div to the result div
            resultsDiv.appendChild(segmentDiv);
        });
    }
}
