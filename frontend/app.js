/ BUG: Missing React imports - will fail ESLint
// Uncomment bugs below to test ESLint scenario:
// import React from 'react';
// import { useState, useEffect } from 'react';

function Dashboard() {
    // BUG: These will fail if imports are missing
    // const [data, setData] = useState([]);
    
    // useEffect(() => {
    //     console.log('Loading data...'); // Will fail ESLint (no-console)
    //     fetchData();
    // }, []);
    
    return (
        
            Dashboard
        
    );
}

export default Dashboard;