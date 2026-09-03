async function sb_test() {
  alert("Starting to send to SB - v3")
  const url = "https://nrkfgubozcjiujdusruu.supabase.co/rest/v1/coa"
  const key = "sb_publishable_7g8lyiXKxmq27-bBV-dcOg_jCYLNc1i"
  const jv_data = {
  "account_name": "Test",
  "account_type": "Liability",
  "parent_id": 2,
  "is_group": 1
  }
  
  const response = await fetch(
    url, 
    {method: "POST",
      headers: {
        "apikey": key,
        "Authorization": `Bearer ${key}`,
        "Content-Type": "application/json",
        "Prefer": "return=representation"
      },
      body: JSON.stringify(jv_data)
    });
    
    const data = await response.json();
    
    console.log(data);
    };