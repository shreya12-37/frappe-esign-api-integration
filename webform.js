frappe.web_form.after_save = () => {
    //var url = "https://www.esigngenie.com/esign/onlineforms/fillOnlineForm?encformnumber=zb1TyQA9CaG58Foonv0%2Fqg%3D%3D&type=link";
    //window.location.replace(url); 
    console.log("Inside")
    frappe.call({
            method: "esign",
            args: {
                company : frappe.web_form.get_value('supplier_name')
            },
            type: "POST",
            async: false,
            callback: function(res){
                console.log("api is running",res);
                console.log("Ye aaya URL",res.message.embeddedSigningSessions[0].embeddedSessionURL);
                console.log("ye hai folder ID",res.message.folder.folderId);
                var folder_id = res.message.folder.folderId;
                
            },
            //error: function(e){
            //    console.log("some error",e)
            //}
        })
}
