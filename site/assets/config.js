window.VS_CONFIG = {
  apiBaseUrl: "",
  supabaseUrl: "",
  supabaseAnonKey: "",
  defaultLanguage: "it",
  supportedLanguages: ["it","en","de"],
  visiEndpoint: "",
  publicContentEndpoint: ""
};

(function(){
  try{
    var s=document.createElement('script');
    s.src='assets/home-news.js?v=20260822b';
    s.defer=true;
    document.head.appendChild(s);
  }catch(e){}
})();

/*
 IMPORTANT:
 - Non inserire service_role, password, API segrete o chiavi private.
 - supabaseAnonKey può essere usata solo quando RLS/policy pubbliche sono correttamente configurate.
 - Il backend VìSì deve restare server-side.
*/
